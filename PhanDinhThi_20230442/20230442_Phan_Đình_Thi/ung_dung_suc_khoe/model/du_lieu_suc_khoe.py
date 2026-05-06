import pandas as pd
import os
from datetime import datetime


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
FILE_PATH = os.path.join(DATA_DIR, "suc_khoe.csv")

os.makedirs(DATA_DIR, exist_ok=True)

class DuLieuSucKhoe:
    def __init__(self):
        if not os.path.exists(FILE_PATH):
            df = pd.DataFrame(columns=["thoi_gian", "can_nang", "chieu_cao", "bmi", "nhip_tim", "spo2", "co2"])
            df.to_csv(FILE_PATH, index=False, encoding='utf-8')

    def luu(self, can_nang, chieu_cao, bmi, nhip_tim, spo2, co2):
        try:
            df = pd.read_csv(FILE_PATH)
        except pd.errors.EmptyDataError:
            df = pd.DataFrame(columns=["thoi_gian", "can_nang", "chieu_cao", "bmi", "nhip_tim", "spo2", "co2"])
        
        new_row = {
            "thoi_gian": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "can_nang": can_nang,
            "chieu_cao": chieu_cao,
            "bmi": bmi,
            "nhip_tim": nhip_tim,
            "spo2": spo2,
            "co2": co2
        }
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df.to_csv(FILE_PATH, index=False, encoding='utf-8')

    def doc(self):
        try:
            df = pd.read_csv(FILE_PATH)
            return df if not df.empty else pd.DataFrame(columns=["thoi_gian", "can_nang", "chieu_cao", "bmi", "nhip_tim", "spo2", "co2"])
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=["thoi_gian", "can_nang", "chieu_cao", "bmi", "nhip_tim", "spo2", "co2"])