import csv

def dms_to_decimal(dms_str):
    d, m, s = dms_str.replace("°", " ").replace("′", " ").replace("″", "").split()
    return float(d) + float(m)/60 + float(s)/3600

with open("coord_data.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

with open("转换结果.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["编号", "经度（十进制）", "纬度（十进制）", "备注"])
    for line in lines:
        parts = line.strip().split()
        编号 = parts[0]
        经度_dms = parts[1]
        纬度_dms = parts[2]
        备注 = " ".join(parts[3:])
        经度 = dms_to_decimal(经度_dms)
        纬度 = dms_to_decimal(纬度_dms)
        writer.writerow([编号, 经度, 纬度, 备注])

print("✅ 转换完成，已生成转换结果.csv")
