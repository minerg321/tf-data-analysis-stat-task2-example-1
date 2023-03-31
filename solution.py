import numpy as np
from scipy.stats import norm


chat_id = 575072396 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Определение уровня доверия и расчет соответствующих статистик
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))

    # Вычисление квантилей нормального распределения
    z_upper = norm.ppf(1 - alpha / 2)
    z_lower = norm.ppf(alpha / 2)

    # Вычисление границ интервала
    lower_bound = loc + z_lower * scale
    upper_bound = loc + z_upper * scale
    
    # Возвращение оптимальной интервальной оценки
    return lower_bound, upper_bound
