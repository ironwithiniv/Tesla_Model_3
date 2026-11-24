# Сервисная документация Tesla Model 3 (service.tesla.com)

Скачано **2026-11-24** с публичного портала service.tesla.com. Вход не нужен. Скачан только текст страниц (HTML без навигации). Картинки и видео остались на сервере Tesla: ссылки в HTML абсолютные, поэтому при открытии страницы с интернетом всё подгрузится.

| Папка | Документ | Страниц | Оригинал |
|---|---|---|---|
| `2017-2023_en-us/` | Model 3 Service Manual (кузов до рестайлинга, включая 2021–2023) | 1241 | https://service.tesla.com/docs/Model3/ServiceManual/en-us/index.html |
| `2024+_Highland_en-us/` | Model 3 2024+ Service Manual (Highland) | 1072 | https://service.tesla.com/docs/Model3/ServiceManual/2024/en-us/index.html |
| `Body_Repair_2017-2023_en-us/` | 2017–2023 Model 3 Collision Repair Procedures (Body Repair Manual) | 498 | https://service.tesla.com/docs/BodyRepair/Body_Repair_Procedures/Model_3/HTML/en-us/index.html |
| `Body_Repair_2024+_en-us/` | 2024+ Model 3 Collision Repair Procedures | 308 | https://service.tesla.com/docs/BodyRepair/Body_Repair_Procedures/Model_3_2024/HTML/en-us/index.html |
| `Public_PDF/` | Service Mode User Guide, схемы диагностического кабеля, мастер-лист инструмента и стандарты программы кузовного ремонта Tesla | 4 PDF | https://service.tesla.com/docs/Public/ |

В каждой папке мануала:
- `TOC.md`: оглавление со ссылками на локальные страницы;
- `_page_index.tsv`: файл → заголовок → URL оригинала;
- `html/`: страницы. В шапке каждой указан URL оригинала и дата скачивания.

Текст для поиска лежит в [`../Search-Text/`](../Search-Text/).

## Electrical Reference: ревизии производства (SOP)

Electrical Reference — интерактивное JS-приложение (схемы и разъёмы), офлайн его не сохранить. Ниже ссылки и **таблица ревизий**. По ней видно, к какой «версии» электрики относится машина по дате производства. Источник: https://service.tesla.com/docs/Model3/ElectricalReference/index.html, просмотрено 2026-11-24.

| Ревизия | Фремонт (США) | Шанхай | Схемы / разъёмы |
|---|---|---|---|
| SOP1 | 2017-07-01 – 2018-07-10 | — | [prog-13](https://service.tesla.com/docs/Model3/ElectricalReference/prog-13/interactive/html/index.html) |
| SOP2 | 2018-07-11 – 2019-01-04 | — | [prog-18](https://service.tesla.com/docs/Model3/ElectricalReference/prog-18/interactive/html/index.html) |
| SOP3 | 2019-01-05 – 2019-06-04 | — | [prog-220](https://service.tesla.com/docs/Model3/ElectricalReference/prog-220/interactive/html/index.html) |
| SOP4 | 2019-06-05 – 2020-10-04 | 2019-10-18 – 2020-12-27 | [prog-20](https://service.tesla.com/docs/Model3/ElectricalReference/prog-20/interactive/html/index.html) |
| **SOP5** | **2020-10-05 – 2022-01-16** | 2020-12-28 – 2021-06-15 | [prog-56](https://service.tesla.com/docs/Model3/ElectricalReference/prog-56/interactive/html/index.html) |
| SOP6 | — | 2021-06-16 – 2021-11-11 | [prog-219](https://service.tesla.com/docs/Model3/ElectricalReference/prog-219/interactive/html/index.html) |
| **SOP7** | **2022-01-17 – 2023-12-31** | 2021-11-12 – 2023-08-31 | [prog-187](https://service.tesla.com/docs/Model3/ElectricalReference/prog-187/interactive/html/index.html) |
| **SOP8** (Highland) | **2024-01-01 – 2025-10-03** | 2023-09-01 – 2025-09-12 | [prog-233](https://service.tesla.com/docs/Model3/ElectricalReference/prog-233/interactive/html/index.html) |
| SOP9 | 2025-10-04 – 2026-09-09 | 2025-09-13 – н.в. | [prog-333](https://service.tesla.com/docs/Model3/ElectricalReference/prog-333/interactive/html/index.html) |
| SOP9 «Separated with Bridge» | 2026-09-10 – н.в. | — | [prog-358](https://service.tesla.com/docs/Model3/ElectricalReference/prog-358/interactive/html/index.html) |

Для LR AWD 2021–2023 из Фремонта (VIN начинается с `5YJ3`) это **SOP5** или **SOP7**: граница проходит по дате производства 2022-01-17. Дата есть на табличке в проёме водительской двери. Китайские машины (VIN `LRW3`) идут по колонке «Шанхай».

> Совпадение SOP5/SOP7 с переходом на литиевую 12V АКБ и Ryzen пока не проверено. Это предмет [Buying_Checklist](../Guides/Buying_Checklist.md).

## Поиск

```bash
grep -n -i "upper control arm" Search-Text/ServiceManual_2017-2023.txt | head
grep -n -B3 -A3 "Nm" Search-Text/ServiceManual_2017-2023.txt | less
```

Каждая страница в текстовом файле начинается со строки `===== <заголовок> | <URL> =====`.
