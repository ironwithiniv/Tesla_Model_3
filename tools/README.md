# Скрипты сборки базы

| Скрипт | Что делает |
|---|---|
| `nhtsa_docs.py NHTSA` | Качает PDF отзывов, TSB, расследований по `NHTSA/raw/safety_*.json` (пропускает выгрузки Owner's Manual и файлы > 20 МБ) |
| `nhtsa_summary.py NHTSA` | Строит `NHTSA/README.md` и CSV-сводки |
| `complaint_themes.py NHTSA/raw` | Подсчёт тем жалоб для `Guides/Known_Issues_by_Year.md` |
| `crawl_sm.py BASE_URL OUT` | Краулер мануалов service.tesla.com (GUID-*.html) |
| `trim_sm.py DIR BASE_URL OUT.txt` | Обрезает страницы до содержимого, делает `TOC.md`, `_page_index.tsv` и текст для `Search-Text/` |
| `torque.py DIR OUT.csv`, `torque_md.py OUT.md` | Таблицы моментов затяжки из страниц «Torque Specifications» |

Скрипты, которые читают скачанные файлы, запускать через `python3 -I`.
| `frt.py SEARCH_TXT OUT.csv` | Нормо-часы Tesla (Correction code + FRT) из текстов мануалов |
| `repair_costs.py` | Таблица `Guides/data/repair_jobs.md`: цены EPC × нормо-часы |
