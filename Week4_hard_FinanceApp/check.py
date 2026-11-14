from decimal import Decimal, getcontext
from math import ceil, sqrt

getcontext().prec = 40
D = Decimal

cohorts = [
    ("Q1 2022", D("180000"), D("86400")),
    ("Q2 2022", D("210000"), D("94500")),
    ("Q3 2022", D("240000"), D("100800")),
    ("Q4 2022", D("270000"), D("102600")),
    ("Q1 2023", D("300000"), D("105000")),
]

countries = [
    ("A", D("8"), D("4.5"), D("0.40")),
    ("B", D("12"), D("6.0"), D("0.25")),
    ("C", D("15"), D("7.5"), D("0.15")),
    ("D", D("18"), D("9.0"), D("0.12")),
    ("E", D("25"), D("13.5"), D("0.08")),
]

features = [
    ("Только учет", D("0.60"), D("0.25")),
    ("Учет + инвестиции", D("0.15"), D("0.58")),
    ("Учет + кредиты", D("0.10"), D("0.32")),
    ("Все функции", D("0.15"), D("0.72")),
]

retention = [active / new for _, new, active in cohorts]
churn = [D(1) - r for r in retention]
mean_retention = sum(retention) / D(len(retention))
mean_churn = sum(churn) / D(len(churn))
total_new = sum(new for _, new, _ in cohorts)
total_active = sum(active for _, _, active in cohorts)
weighted_retention = total_active / total_new

assert retention == [D(".48"), D(".45"), D(".42"), D(".38"), D(".35")]
assert mean_churn == D(".584")
assert mean_retention + mean_churn == 1
assert total_new == D("1200000")
assert total_active == D("489300")
assert total_new - total_active == D("710700")
assert weighted_retention == D(".40775")
assert sum(share for _, _, _, share in countries) == 1
assert sum(share for _, share, _ in features) == 1

print("Когорты, R6 и Churn:")
for (label, _, _), r, c in zip(cohorts, retention, churn):
    print(label, f"R6={r:.2%}", f"Churn={c:.2%}")
print("Средний Churn:", f"{mean_churn:.2%}")
print("Взвешенный Retention:", f"{weighted_retention:.3%}")

print("Страна, LTV, LTV/CAC, LTV-CAC:")
ratios = {}
for label, cac, arpu, share in countries:
    ltv = arpu / mean_churn
    ratios[label] = ltv / cac
    print(label, f"${ltv:.2f}", f"{ltv / cac:.3f}", f"${ltv-cac:.2f}")

# Деление Decimal может различаться в самом последнем разряде.
assert abs(ratios["B"] - ratios["C"]) < D("1e-35")
assert abs(ratios["C"] - ratios["D"]) < D("1e-35")
assert ratios["A"] > ratios["E"] > ratios["B"]

mix_proxy = sum(share * r for _, share, r in features)
multi_proxy = (
    sum(share * r for _, share, r in features[1:])
    / sum(share for _, share, _ in features[1:])
)
assert mix_proxy == D(".377")
assert multi_proxy == D(".5675")

shift_all = D(".10") * (D(".58") - D(".25"))
shift_basic = D(".60") * D(".10") * (D(".58") - D(".25"))
improve_basic = D(".60") * (D(".30") - D(".25"))
assert shift_all == D(".033")
assert shift_basic == D(".0198")
assert improve_basic == D(".030")

print("Условный показатель состава:", f"{mix_proxy:.2%}")
print("Условный показатель нескольких функций:", f"{multi_proxy:.2%}")
print("Дополнительные удержанные на условные 100000:")
for label, lift in [
    ("Улучшение учета", improve_basic),
    ("Переход 10 п.п. всей базы", shift_all),
    ("Переход 10% базового сегмента", shift_basic),
]:
    print(label, D("100000") * lift)

# Альтернативная модель только при месячном ARPU,
# постоянном месячном Churn и отсутствии реактивации.
monthly_churn = 1 - float(mean_retention) ** (1 / 6)
print("Сценарный месячный Churn:", f"{monthly_churn:.6%}")
for label, _, arpu, _ in countries:
    print(label, "сценарный месячный LTV", f"${float(arpu)/monthly_churn:.2f}")

# Нормальная аппроксимация объема одного A/B-теста.
p0, p1 = 0.25, 0.30
pbar = (p0 + p1) / 2
z_alpha, z_power = 1.959963984540054, 0.8416212335729143
n = (
    z_alpha * sqrt(2 * pbar * (1 - pbar))
    + z_power * sqrt(p0 * (1 - p0) + p1 * (1 - p1))
) ** 2 / (p1 - p0) ** 2
assert ceil(n) == 1251
print("Расчетный размер одной группы:", ceil(n))
print("Все арифметические проверки пройдены.")
