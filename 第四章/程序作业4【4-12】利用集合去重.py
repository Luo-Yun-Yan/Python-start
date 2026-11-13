mon = ["语文", "数学", "体育", "信息技术", "语文", "生物", "物理", "历史"]
tue = ["数学", "道德与法律", "语文", "体育", "物理", "历史", "音乐", "英语"]
wed = ["英语", "语文", "数学", "地理", "体育", "英语", "生物", "历史"]
thu = ["语文", "英语", "道德与法律", "数学", "语文", "地理", "物理", "信息技术"]
fri = ["数学", "英语", "语文", "数学", "体育", "道德与法律", "美术", "劳动"]

courses = []
courses.extend(mon)
courses.extend(tue)
courses.extend(wed)
courses.extend(thu)
courses.extend(fri)

unicourses = set(courses)

print("=== 课程统计结果 ===")
print(f"总科目数: {len(unicourses)}")
print("科目列表:", sorted(unicourses))