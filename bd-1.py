{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1-р хугацаа (1978-1988):\n",
      "  Дунд сургуулийн цаг: 9184.5 цаг\n",
      "  Их сургуулийн цаг: 5265.0 цаг\n",
      "2-р хугацаа (2006-2018):\n",
      "  Дунд сургуулийн цаг: 6727.5 цаг\n",
      "  Их сургуулийн цаг: 3510.0 цаг\n",
      "\n",
      "Сонирхсон хичээлийн цагийн харьцуулалт:\n",
      "  1-р хугацаа (1978-1988): 1560 цаг\n",
      "  2-р хугацаа (2006-2018): 1872 цаг\n",
      "\n",
      "Дадлагын хувь харьцуулалт:\n",
      "  1-р хугацаа (1978-1988): 20.51%\n",
      "  2-р хугацаа (2006-2018): 20.51%\n"
     ]
    }
   ],
   "source": [
    "# Тогтмол утгуудыг тодорхойлно\n",
    "weeks_per_year = 39  # Хичээлийн жилд 39 долоо хоног гэж үзнэ (9 сарын 1-нээс 6 сарын 1 хүртэл)\n",
    "\n",
    "# 1-р хугацааны судалгаа (1978-1988)\n",
    "def study_period_1():\n",
    "    # Дунд сургууль (10 жил)\n",
    "    sec_school_hours = 0\n",
    "    # 1-3-р анги: Өдөрт 4 цаг, 7 хоногт 6 өдөр хичээллэнэ, нэг цаг 45 минут үргэлжилнэ\n",
    "    sec_school_hours += 3 * weeks_per_year * 6 * 4 * 0.75\n",
    "    \n",
    "    # 4-8-р анги: 7 хоногт нийт 34 цаг хичээлтэй, нэг цаг 45 минут үргэлжилнэ\n",
    "    sec_school_hours += 5 * weeks_per_year * 34 * 0.75\n",
    "    \n",
    "    # 9-10-р анги: Өдөрт 6 цаг, 7 хоногт 6 өдөр хичээллэнэ, нэг цаг 45 минут үргэлжилнэ\n",
    "    sec_school_hours += 2 * weeks_per_year * 6 * 6 * 0.75\n",
    "\n",
    "    # Их сургууль (5 жил)\n",
    "    uni_hours = 5 * weeks_per_year * 6 * 3 * 1.5  # Өдөрт 3 цаг, нэг цаг 90 минут үргэлжилнэ\n",
    "\n",
    "    return sec_school_hours, uni_hours\n",
    "\n",
    "\n",
    "# 2-р хугацааны судалгаа (2006-2018)\n",
    "def study_period_2():\n",
    "    # Дунд сургууль (12 жил)\n",
    "    sec_school_hours = 0\n",
    "    # 1-5-р анги: Өдөрт 4 цаг, 7 хоногт 5 өдөр хичээллэнэ, нэг цаг 30 минут үргэлжилнэ\n",
    "    sec_school_hours += 5 * weeks_per_year * 5 * 4 * 0.5\n",
    "    \n",
    "    # 6-12-р анги: Өдөрт 6 цаг, 7 хоногт 5 өдөр хичээллэнэ, нэг цаг 35 минут үргэлжилнэ\n",
    "    sec_school_hours += 7 * weeks_per_year * 5 * 6 * (35 / 60)\n",
    "\n",
    "    # Их сургууль (4 жил)\n",
    "    uni_hours = 4 * weeks_per_year * 5 * 3 * 1.5  # Өдөрт 3 цаг, нэг цаг 90 минут үргэлжилнэ\n",
    "\n",
    "    return sec_school_hours, uni_hours\n",
    "                 \n",
    "# Сонирхсон хичээлийн цагийг тооцоолох функц\n",
    "def interest_hours(study_years):\n",
    "    full_weeks = weeks_per_year  # Хичээлийн жил бүрийн 39 бүтэн долоо хоног гэж тооцно\n",
    "    return study_years * full_weeks * 4  # Долоо хоногт 4 цагийн хичээл сонирхолдоо зориулагдсан гэж үзнэ\n",
    "\n",
    "# Дадлагын хувь тооцоолох функц\n",
    "def internship_percentage(uni_years, internship_weeks):\n",
    "    total_study_weeks = weeks_per_year * uni_years  # Нийт хичээлийн долоо хоногийн тоо\n",
    "    return (internship_weeks * uni_years) / total_study_weeks * 100  # Дадлагын эзлэх хувийг олно\n",
    "\n",
    "# Хоёр хугацааны судалгааны нийт цагийг тооцно\n",
    "sec_hours_1, uni_hours_1 = study_period_1()\n",
    "sec_hours_2, uni_hours_2 = study_period_2()\n",
    "\n",
    "# Дунд болон их сургуулийн хичээллэх цагийн харьцуулалт\n",
    "print(\"1-р хугацаа (1978-1988):\")\n",
    "print(f\"  Дунд сургуулийн цаг: {sec_hours_1} цаг\")\n",
    "print(f\"  Их сургуулийн цаг: {uni_hours_1} цаг\")\n",
    "\n",
    "print(\"2-р хугацаа (2006-2018):\")\n",
    "print(f\"  Дунд сургуулийн цаг: {sec_hours_2} цаг\")\n",
    "print(f\"  Их сургуулийн цаг: {uni_hours_2} цаг\")\n",
    "\n",
    "# Дунд сургуульд сонирхсон хичээлийн цагийг харьцуулах\n",
    "interest_hours_1 = interest_hours(10)  # 1-р хугацаанд дунд сургууль 10 жил\n",
    "interest_hours_2 = interest_hours(12)  # 2-р хугацаанд дунд сургууль 12 жил\n",
    "print(\"\\nСонирхсон хичээлийн цагийн харьцуулалт:\")\n",
    "print(f\"  1-р хугацаа (1978-1988): {interest_hours_1} цаг\")\n",
    "print(f\"  2-р хугацаа (2006-2018): {interest_hours_2} цаг\")\n",
    "\n",
    "# Их сургуульд дадлагын хувийг тооцох\n",
    "internship_percent_1 = internship_percentage(5, 8)  # 1-р хугацаанд 5 жил, 8 долоо хоногийн дадлага\n",
    "internship_percent_2 = internship_percentage(4, 8)  # 2-р хугацаанд 4 жил, 8 долоо хоногийн дадлага\n",
    "print(\"\\nДадлагын хувь харьцуулалт:\")\n",
    "print(f\"  1-р хугацаа (1978-1988): {internship_percent_1:.2f}%\")\n",
    "print(f\"  2-р хугацаа (2006-2018): {internship_percent_2:.2f}%\")\n",
    "#13:19"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13 (main, Aug 25 2022, 18:29:29) \n[Clang 12.0.0 ]"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "e5f7f93e8ed9a7c2075c4e010597b69de4533f30c1ef2f8f66344419f45e941e"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}