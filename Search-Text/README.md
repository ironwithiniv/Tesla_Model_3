# Текстовые выгрузки для поиска

Плоский текст всех собранных документов. Искать удобно через `grep -n -i`. Страницы и документы разделены строками `===== <заголовок> | <источник> =====`.

| Файл | Источник |
|---|---|
| `ServiceManual_2017-2023.txt` | Service Manual Model 3 2017–2023, 1241 страница ([../Service-Manual/2017-2023_en-us](../Service-Manual/2017-2023_en-us)) |
| `ServiceManual_2024+_Highland.txt` | Service Manual Model 3 2024+, 1072 страницы |
| `BodyRepair_2017-2023.txt`, `BodyRepair_2024+.txt` | Collision Repair Procedures (Body Repair Manual) |
| `service_mode_user_guide.txt` | Service Mode User Guide (Tesla, PDF) |
| `Tesla_Diagnostic_Cable_Schematics.txt` | Схемы диагностических кабелей |
| `Tesla_Approved_Body_Shops_Global_Master_Tooling_List.txt`, `Tesla_Body_Repair_Program_Operating_Standards.txt` | Требования Tesla к кузовным цехам |
| `NHTSA_TSB.txt` | 47 технических бюллетеней (PDF из `../NHTSA/TSB`) |
| `NHTSA_Recalls.txt` | Документы 29 отзывов |
| `NHTSA_Investigations.txt` | Резюме расследований ODI |

Owner's Manual сюда добавится после того, как PDF будут скачаны вручную (см. [../Owner-Manual/README.md](../Owner-Manual/README.md)).

```bash
grep -n -i "cabin air filter" Search-Text/*.txt | head
grep -n -i -A4 "brake fluid" Search-Text/ServiceManual_2017-2023.txt | grep -i "interval\|every\|year"
```
