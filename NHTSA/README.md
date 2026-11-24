# NHTSA: Tesla Model 3, 2021–2024 (AWD)

Источник: api.nhtsa.gov, выгрузка **2026-11-24**. Данные NHTSA одинаковы для RWD и AWD одного года (общий список по модели).

| Файл / папка | Что внутри |
|---|---|
| `raw/recalls_YYYY.json` | `recalls/recallsByVehicle` (публичный API) |
| `raw/complaints_YYYY.json` | `complaints/complaintsByVehicle`, все жалобы владельцев |
| `raw/safety_YYYY.json` | `vehicles/byYmmt` (API сайта nhtsa.gov): отзывы + расследования + manufacturer communications (TSB) |
| [recalls.csv](recalls.csv) | Сводка отзывов |
| [tsb_manufacturer_communications.csv](tsb_manufacturer_communications.csv) | Сводка TSB / Manufacturer Communications |
| [investigations.csv](investigations.csv) | Расследования ODI (PE/EA/RQ/DP) |
| `Recalls/<кампания>/`, `TSB/<nhtsaId>/`, `Investigations/<номер>/` | PDF-документы с static.nhtsa.gov |
| `*_index.json` | Индекс документов по каждой записи (со ссылками и на нескачанные файлы) |

По расследованиям скачаны только ключевые документы: `INOA` (резюме открытия), `INCLA` (резюме закрытия), `INRL` (связанный отзыв). Переписка ODI с Tesla не скачана, ссылки в `Investigations_index.json`. Файлы больше 20 МБ тоже не скачаны.

## Количество записей

| Модельный год | Жалобы | Отзывы | Расследования | TSB (MC) |
|---|---|---|---|---|
| 2021 | 680 | 22 | 13 | 85 |
| 2022 | 777 | 18 | 13 | 76 |
| 2023 | 434 | 12 | 13 | 76 |
| 2024 | 224 | 5 | 7 | 58 |

Уникальных записей за 2021–2024: отзывов **29**, расследований **17**, TSB **101**. В жалобах: с ДТП 204, с пожаром 11, пострадавших 135.

## Отзывы (recalls)

| Кампания NHTSA | № Tesla | Дата | Годы | OTA | Суть |
|---|---|---|---|---|---|
| [26V507000](https://www.nhtsa.gov/recalls?nhtsaId=26V507000) | SB-24-17-003 | 2026-08-05 | 2021, 2022, 2023 | нет | Low Beam Headlights May Be Too Bright/FMVSS 108 |
| [26V445000](https://www.nhtsa.gov/recalls?nhtsaId=26V445000) | SB-26-00-004 | 2026-07-07 | 2024 | нет | Noncompliant Vehicles Incorrectly Imported/FMVSS 208, 201 |
| [26V283000](https://www.nhtsa.gov/recalls?nhtsaId=26V283000) | SB-26-00-001 | 2026-05-05 | 2021, 2022, 2023 | нет | Rearview Camera Image May Not Display/FMVSS 111 |
| [25V092000](https://www.nhtsa.gov/recalls?nhtsaId=25V092000) | SB-25-00-004 | 2025-02-15 | 2023 | да | Loss of Power Steering Assist |
| [25V002000](https://www.nhtsa.gov/recalls?nhtsaId=25V002000) | SB-25-00-001 | 2025-01-07 | 2024 | нет | Rearview Camera Image May Fail/FMVSS 111 |
| [24V935000](https://www.nhtsa.gov/recalls?nhtsaId=24V935000) | SB-24-00-018 | 2024-12-17 | 2021, 2022, 2023, 2024 | да | TPMS Light May Not Remain Illuminated/FMVSS 138 |
| [24V554000](https://www.nhtsa.gov/recalls?nhtsaId=24V554000) | SB-24-00-012 | 2024-07-24 | 2021, 2022, 2023, 2024 | да | Software May Fail to Detect Unlatched Hood |
| [24V376000](https://www.nhtsa.gov/recalls?nhtsaId=24V376000) | SB-24-00-008 | 2024-05-28 | 2021, 2022, 2023 | да | Seat Belt Warning System Malfunction/FMVSS 208 |
| [24V284000](https://www.nhtsa.gov/recalls?nhtsaId=24V284000) | SB-24-13-001 | 2024-04-19 | 2024 | нет | Driver's Side Air Bag May Deploy Improperly |
| [24V153000](https://www.nhtsa.gov/recalls?nhtsaId=24V153000) | SB-24-00-006 | 2024-02-27 | 2021, 2022 | да | Muted Pedestrian Warning Sound/FMVSS 141 |
| [24V051000](https://www.nhtsa.gov/recalls?nhtsaId=24V051000) | SB-24-00-003 | 2024-01-30 | 2021, 2022, 2023 | да | Incorrect Font Size on Warning Lights/FMVSS 105 |
| [23V838000](https://www.nhtsa.gov/recalls?nhtsaId=23V838000) | SB-23-00-008 | 2023-12-12 | 2021, 2022, 2023 | да | Autopilot Controls Insufficient to Prevent Misuse |
| [23V434000](https://www.nhtsa.gov/recalls?nhtsaId=23V434000) | SB-23-16-005 | 2023-06-19 | 2023 | нет | Defective Pyrotechnic Battery Disconnect |
| [23V085000](https://www.nhtsa.gov/recalls?nhtsaId=23V085000) | SB-23-00-001 | 2023-02-15 | 2021, 2022, 2023 | да | Full Self-Driving Software May Cause Crash |
| [22V844000](https://www.nhtsa.gov/recalls?nhtsaId=22V844000) | SB-22-00-016 | 2022-11-15 | 2023 | да | Taillight May Fail to Illuminate |
| [22V798000](https://www.nhtsa.gov/recalls?nhtsaId=22V798000) | SB-22-20-004 | 2022-10-21 | 2021, 2022 | нет | Seat Belt Buckle, Anchor Incorrectly Reassembled |
| [22V702000](https://www.nhtsa.gov/recalls?nhtsaId=22V702000) | SB-22-00-013 | 2022-09-19 | 2021, 2022 | да | Power Windows May Pinch/FMVSS 118 |
| [22V317000](https://www.nhtsa.gov/recalls?nhtsaId=22V317000) | SB-22-17-007 | 2022-05-09 | 2021 | нет | Fisheye and Narrow Camera Views Swapped |
| [22V296000](https://www.nhtsa.gov/recalls?nhtsaId=22V296000) | SB-22-00-009 | 2022-05-03 | 2022 | да | Overheating May Cause Center Display Malfunction |
| [22V263000](https://www.nhtsa.gov/recalls?nhtsaId=22V263000) | SB-22-00-008 | 2022-04-18 | 2021, 2022 | да | Unit of Speed May Fail to Display/FMVSS 101 |
| [22V235000](https://www.nhtsa.gov/recalls?nhtsaId=22V235000) | SB-22-00-003 | 2022-04-12 | 2021, 2022 | да | Pedestrian Warning Sound May Be Obscured/FMVSS 141 |
| [22V063000](https://www.nhtsa.gov/recalls?nhtsaId=22V063000) | SB-22-00-003 | 2022-02-04 | 2021, 2022 | да | Pedestrian Warning Sound May Be Obscured/FMVSS 141 |
| [22V050000](https://www.nhtsa.gov/recalls?nhtsaId=22V050000) | SB-22-18-002 | 2022-02-02 | 2021, 2022 | да | Windshield May Not Defrost Properly/FMVSS 103 |
| [22V045000](https://www.nhtsa.gov/recalls?nhtsaId=22V045000) | SB-22-00-002 | 2022-02-01 | 2021, 2022 | да | Seat Belt Chime May Not Activate/FMVSS 208 |
| [22V037000](https://www.nhtsa.gov/recalls?nhtsaId=22V037000) | SB-22-00-001 | 2022-01-27 | 2021, 2022 | да | Vehicle May Fail to Stop at Stop Sign |
| [21V846000](https://www.nhtsa.gov/recalls?nhtsaId=21V846000) | SB-21-00-004 | 2021-10-29 | 2021 | да | Unexpected Activation of Automatic Emergency Brake |
| [21V835000](https://www.nhtsa.gov/recalls?nhtsaId=21V835000) | SB-21-31-003 | 2021-10-25 | 2021 | нет | Front Suspension Lateral Link May Separate |
| [21V834000](https://www.nhtsa.gov/recalls?nhtsaId=21V834000) | SB-21-20-006 | 2021-10-25 | 2021, 2023 | нет | Side Curtain Air Bag May Be Twisted/FMVSS 214, 226 |
| [21V387000](https://www.nhtsa.gov/recalls?nhtsaId=21V387000) | SB-21-33-002 | 2021-05-25 | 2021 | нет | Loose Brake Caliper Bolts |

## Расследования ODI

| Номер | Открыто | Закрыто | Годы | Тема |
|---|---|---|---|---|
| EA26002 |  | открыто | 2021, 2022, 2023, 2024 | FSD Collisions in Reduced Roadway Visibility Conditions |
| PE25012 |  | открыто | 2021, 2022, 2023, 2024 | Traffic safety violations while Full Self Driving ("FSD") is engaged |
| AQ25002 |  | открыто | 2021, 2022, 2023, 2024 | Compliance with Standing General Order 2021-01 Reporting Requirements |
| PE24033 |  | открыто | 2021, 2023, 2024 | Actually Smart Summon sessions resulting in low-speed impacts. |
| PE24031 |  | открыто | 2021, 2022, 2023, 2024 | FSD Collisions in Reduced Roadway Visibility Conditions |
| RQ24009 |  | открыто | 2021, 2022, 2023, 2024 | Recall 23V838 Remedy Effectiveness |
| DP23002 |  | открыто | 2021, 2022, 2023 | Sudden Unintended Acceleration |
| DP23001 |  | открыто | 2021, 2022, 2023 | Defect Petition Interlock Request |
| DP22005 |  | открыто | 2021, 2022 | Pedestrian alert sounds |
| EA22002 |  | открыто | 2021, 2022, 2023 | Autopilot System Driver Controls |
| PE22002 |  | открыто | 2021, 2022, 2023, 2024 | Unexpected Brake Activation |
| PE21023 |  | открыто | 2021, 2022 | Tesla Passenger Play |
| PE21020 |  | открыто | 2021, 2022 | Autopilot & First Responder Scenes |
| DP25002 |  | открыто | 2022 | Emergency egress controls are not readily accessible and clearly identifiable. |
| PE26006 |  | открыто | 2023 | Lower Lateral Link detachment |
| EA24001 |  | открыто | 2023 | Loss of steering control |
| PE23014 |  | открыто | 2023 | Loss of steering control |

## TSB / Manufacturer Communications

Полный текст аннотаций в CSV, PDF в `TSB/<nhtsaId>/`. **54 из 101** записей — это не бюллетени, а выгрузки Owner's Manual под каждую версию ПО (PDF по ~46 МБ на 1500+ страниц, все модели сразу). Их PDF не скачаны, ссылки есть в `TSB_index.json`. В таблице ниже только технические бюллетени.

| nhtsaId | № Tesla | Дата | Годы | Узел | Кратко |
|---|---|---|---|---|---|
| [11034277](TSB/11034277/) | SB-26-13-005 | 2026-06-04 | 2024 | SEATS | On some vehicles, degraded or excessive glue under the front seat cushion(s) may cause creaking noises during cornering or when pressing on the seat cushion(s)… |
| [11033171](TSB/11033171/) | SB-26-13-006 | 2026-05-29 | 2024 | SEATS | On some vehicles, insufficient lubricant at the front seat recliner tube ends may cause creaking noises during weight shifting when the seat is occupied. Upon … |
| [11033173](TSB/11033173/) | SB-26-33-001 | 2026-05-08 | 2021, 2022, 2023 | SERVICE BRAKES | On certain Model 3 vehicles, brake lines may be corroded beyond acceptable limits, which may result in loss of brake fluid. Loss of brake fluid will result in … |
| [11029583](TSB/11029583/) | SB-26-33-001 | 2026-02-11 | 2021, 2022, 2023 | SERVICE BRAKES | On certain Model 3 vehicles, brake lines may be corroded beyond acceptable limits, which may result in loss of brake fluid. Loss of brake fluid will result in … |
| [11020192](TSB/11020192/) | SB-25-31-004 | 2025-06-24 | 2021, 2022, 2023, 2024 | SUSPENSION | A firmware diagnosis feature is being introduced on Model 3 and Model Y vehicles that monitors wheel alignment over time. This feature detects changes in wheel… |
| [11016320](TSB/11016320/) | SB-25-16-001 | 2025-03-20 | 2024 | ELECTRICAL SYSTEM | Certain Model 3 and Model Y vehicles were manufactured with High Voltage (HV) batteries containing cell modules that do not meet Tesla’s internal quality stand… |
| [11011363](TSB/11011363/) | SB-24-33-006 | 2024-11-06 | 2024 | SERVICE BRAKES | On some Model 3 vehicles, the RH front Wheel Speed Sensor (WSS) might have been misrouted, which may cause damage to the WSS harness. |
| [11009776](TSB/11009776/) | SB-24-33-006 | 2024-10-31 | 2024 | SERVICE BRAKES | On some Model 3 vehicles, the RH front Wheel Speed Sensor (WSS) might have been misrouted, which may cause damage to the WSS harness. |
| [11009781](TSB/11009781/) | SB-24-40-008 | 2024-10-15 | 2024 | POWER TRAIN | Some Performance Model 3 vehicles might experience minor oil loss through the Rear Drive Unit (RDU) breather during high lateral acceleration cornering maneuve… |
| [11009773](TSB/11009773/) | SB-24-14-001 | 2024-10-11 | 2024 | ELECTRICAL SYSTEM | On some 2024+ Model 3 vehicles built at Fremont, a rattling noise may be noticed from the driver and/or front passenger instrument panel air vent while the fac… |
| [11008772](TSB/11008772/) | SB-24-16-005 | 2024-09-04 | 2023, 2024 | ELECTRICAL SYSTEM | On certain Model 3 and Model Y vehicles, a defective electrical component inside the High Voltage Controller may prevent the vehicle from entering into drive m… |
| [11008796](TSB/11008796/) | SB-24-16-005 | 2024-09-04 | 2023, 2024 | ELECTRICAL SYSTEM | On certain Model 3 and Model Y vehicles, a defective electrical component inside the High Voltage Controller may prevent the vehicle from entering into drive m… |
| [11008820](TSB/11008820/) | SB-24-16-005 | 2024-09-04 | 2023, 2024 | ELECTRICAL SYSTEM | On certain Model 3 and Model Y vehicles, a defective electrical component inside the High Voltage Controller may prevent the vehicle from entering into drive m… |
| [11006908](TSB/11006908/) | SB-24-14-001 | 2024-08-15 | 2024 | UNKNOWN OR OTHER | On some 2024+ Model 3 built at Fremont, a rattling noise may be noticed from the driver and/or front passenger instrument panel air vent while the face-level a… |
| [11001923](TSB/11001923/) | SB-24-10-005 | 2024-04-16 | 2021, 2022, 2023 | STRUCTURE | Certain Standard Range Model 3 and Model Y vehicles that received the Lithium Iron Phosphate (LFP) HV Battery Retrofit did not receive the 2nd row floor reinfo… |
| [10253653](TSB/10253653/) | SB2118002 | 2024-03-21 | 2021 | VISIBILITY | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10252961](TSB/10252961/) | terminal | 2024-02-19 | 2021, 2022, 2023 | EQUIPMENT | Owner's Manual. |
| [10252956](TSB/10252956/) | developF | 2024-02-13 | 2021, 2022, 2023, 2024 | EQUIPMENT | Owner's Manual. |
| [10252948](TSB/10252948/) | develop | 2024-02-07 | 2021, 2022, 2023, 2024 | EQUIPMENT | Owner's Manual |
| [10245512](TSB/10245512/) | SB-23-32-003 | 2023-10-11 | 2021, 2022, 2023 | STEERING | On some Model 3 and Model Y vehicles, the steering wheel cover material may separate from the steering wheel at the 3 o'clock and 9 o'clock position (Figures 1… |
| [10247387](TSB/10247387/) | SB23-32-003 | 2023-10-11 | 2021, 2022, 2023 | STEERING | On some Model 3 and Model Y vehicles, the steering wheel cover material may separate from the steering wheel at the 3 o'clock and 9 o'clock position (Figures 1… |
| [10243088](TSB/10243088/) | SB2317007R1 | 2023-08-25 | 2023 | STRUCTURE; ELECTRICAL SYSTEM | Certain Model 3 and Model Y vehicles may require replacement of the front body controller module due to a faulty component. |
| [10243087](TSB/10243087/) | SB2317007 | 2023-08-18 | 2023 | STRUCTURE; ELECTRICAL SYSTEM | Certain Model 3 and Model Y vehicles may require replacement of the front body controller module due to a faulty component. |
| [10243082](TSB/10243082/) | SB2320002R6 | 2023-08-02 | 2021, 2022, 2023 | STRUCTURE | Certain Model 3 and Model Y vehicles may need a different Occupant Classification System (OCS) installed in the front passenger seat before servicing its subco… |
| [10240953](TSB/10240953/) | SB2320002R5 | 2023-06-16 | 2021, 2022, 2023 | STRUCTURE | Certain Model 3 and Model Y vehicles may need a different Occupant Classification System (OCS) installed in the front passenger seat before servicing its subco… |
| [10240946](TSB/10240946/) | SB2320002R4 | 2023-06-08 | 2021, 2022, 2023 | STRUCTURE | Certain Model 3 and Model Y vehicles may need a different Occupant Classification System (OCS) installed in the front passenger seat before servicing its subco… |
| [10235969](TSB/10235969/) | SB-23-10-002 R2 | 2023-04-27 | 2021, 2022, 2023 | STRUCTURE | On some Model 3 vehicles, water may have leaked inside the trunk area through the trunk lid. |
| [10235966](TSB/10235966/) | SB-23-10-002 R1 | 2023-04-17 | 2021, 2022, 2023 | STRUCTURE | On some Model 3 vehicles, water may have leaked inside the trunk area through the trunk lid. |
| [10235962](TSB/10235962/) | SB-23-10-002 | 2023-04-05 | 2021, 2022, 2023 | STRUCTURE | On some Model 3 vehicles, water may have leaked inside the trunk area through the trunk lid. |
| [10234057](TSB/10234057/) | SB-23-20-002 R2 | 2023-03-27 | 2021, 2022, 2023 | SEATS; AIR BAGS | Certain Model 3 and Model Y vehicles may need a different Occupant Classification System (OCS) installed in the front passenger seat before servicing its subco… |
| [10234054](TSB/10234054/) | SB-23-16-001 | 2023-03-21 | 2023 | ELECTRICAL SYSTEM | Certain Model 3 and Model Y vehicles may require HV battery replacement because the wire bonds within their HV batteries may not have been manufactured to inte… |
| [10234053](TSB/10234053/) | SB-23-20-002 R1 | 2023-03-15 | 2021, 2022, 2023 | AIR BAGS | Certain Model 3 and Model Y vehicles may need a different Occupant Classification System (OCS) installed in the front passenger seat before servicing its subco… |
| [10234051](TSB/10234051/) | SB-23-20-002 | 2023-03-11 | 2021, 2022, 2023 | SEATS | Certain Model 3 and Model Y vehicles may need a different Occupant Classification System (OCS) installed in the front passenger seat before servicing its subco… |
| [10226577](TSB/10226577/) | SB-21-18-002-R6 | 2022-08-17 | 2021 | ELECTRICAL SYSTEM | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10226576](TSB/10226576/) | SB-22-17-006 | 2022-08-16 | 2022 | ELECTRICAL SYSTEM; STRUCTURE | Certain Model 3 vehicles were equipped with a RH body controller module which might have a damaged component. Though the module is operational, should the comp… |
| [10213756](TSB/10213756/) | SB2233004 | 2022-04-29 | 2021, 2022 | ELECTRONIC STABILITY CONTROL; ELECTRICAL SYSTEM | Some Heat Pump Model 3 vehicles were built without a hydraulic control unit (HCU) wake-up wire, and in rare circumstances, braking and stability control relate… |
| [10213755](TSB/10213755/) | SB2233003 | 2022-04-29 | 2021, 2022 | ELECTRONIC STABILITY CONTROL; ELECTRICAL SYSTEM | Some Heat Pump Model 3 vehicles were built without a hydraulic control unit (HCU) wake-up wire, and in rare circumstances, braking and stability control relate… |
| [10234999](TSB/10234999/) | SB2233003 | 2022-04-29 | 2021, 2022 | FUEL SYSTEM, GASOLINE; ELECTRONIC STABILITY CONTROL; POWER TRAIN | Some Heat Pump Model 3 vehicles were built without a hydraulic control unit (HCU) wake-up wire, and in rare circumstances, braking and stability control relate… |
| [10235000](TSB/10235000/) | SB2233004 | 2022-04-29 | 2021, 2022 | FUEL SYSTEM, GASOLINE; ELECTRONIC STABILITY CONTROL; POWER TRAIN | Some Heat Pump Model 3 vehicles were built without a hydraulic control unit (HCU) wake-up wire, and in rare circumstances, braking and stability control relate… |
| [10210727](TSB/10210727/) | SB2118002R5 | 2022-03-16 | 2021 | FUEL SYSTEM, GASOLINE | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10208324](TSB/10208324/) | SB2116003 | 2021-12-07 | 2021 | ELECTRICAL SYSTEM | Certain Model 3 and Model Y vehicles were manufactured with high voltage (HV) batteries having cell separators that do not meet Tesla?s internal standards of q… |
| [10212799](TSB/10212799/) | SB2116003 | 2021-12-07 | 2021 | HYBRID PROPULSION SYSTEM | Certain Model 3 and Model Y vehicles were manufactured with high voltage (HV) batteries having cell separators that do not meet Tesla?s internal standards of q… |
| [10203343](TSB/10203343/) | SB-21-18-002 R3 | 2021-07-10 | 2021 | ENGINE AND ENGINE COOLING | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10190907](TSB/10190907/) | SB-21-18-002 R1 | 2021-03-05 | 2021 | FUEL SYSTEM, GASOLINE | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10190908](TSB/10190908/) | SB-21-18-001 R1 | 2021-03-05 | 2021 | FUEL SYSTEM, GASOLINE | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10190906](TSB/10190906/) | SB-21-18-002 | 2021-03-01 | 2021 | FUEL SYSTEM, GASOLINE | Certain Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |
| [10189010](TSB/10189010/) | SB-21-18-001 | 2021-02-05 | 2021 | ENGINE AND ENGINE COOLING | Some Model 3 and Model Y vehicles may be equipped with refrigerant pressure/temperature (P/T) sensors in the heat pump that can fault over time. |

## Жалобы по узлам (топ-30)

| Узел (NHTSA) | Всего | 2021 | 2022 | 2023 | 2024 |
|---|---|---|---|---|---|
| FORWARD COLLISION AVOIDANCE | 1179 | 411 | 538 | 181 | 49 |
| VEHICLE SPEED CONTROL | 385 | 123 | 171 | 70 | 21 |
| SERVICE BRAKES | 358 | 127 | 169 | 58 | 4 |
| UNKNOWN OR OTHER | 323 | 97 | 94 | 60 | 72 |
| ELECTRICAL SYSTEM | 244 | 82 | 63 | 52 | 47 |
| STEERING | 199 | 28 | 39 | 92 | 40 |
| LANE DEPARTURE | 125 | 34 | 46 | 28 | 17 |
| VISIBILITY/WIPER | 69 | 34 | 17 | 12 | 6 |
| STRUCTURE | 56 | 18 | 11 | 22 | 5 |
| SUSPENSION | 54 | 18 | 10 | 19 | 7 |
| AIR BAGS | 47 | 8 | 13 | 18 | 8 |
| POWER TRAIN | 46 | 17 | 13 | 12 | 4 |
| EXTERIOR LIGHTING | 43 | 8 | 7 | 1 | 27 |
| SEAT BELTS | 40 | 15 | 12 | 10 | 3 |
| WHEELS | 35 | 6 | 13 | 9 | 7 |
| BACK OVER PREVENTION | 31 | 9 | 8 | 9 | 5 |
| FUEL/PROPULSION SYSTEM | 31 | 10 | 9 | 8 | 4 |
| SEATS | 27 | 6 | 10 | 9 | 2 |
| ENGINE | 24 | 5 | 7 | 8 | 4 |
| LATCHES/LOCKS/LINKAGES | 13 | 7 | 2 | 4 | 0 |
| VISIBILITY | 10 | 2 | 7 | 1 | 0 |
| TIRES | 5 | 3 | 1 | 1 | 0 |
| HYDRAULIC | 3 | 1 | 0 | 2 | 0 |
| ENGINE AND ENGINE COOLING | 2 | 1 | 1 | 0 | 0 |
| EQUIPMENT | 2 | 0 | 2 | 0 | 0 |
| FIRERELATED | 1 | 1 | 0 | 0 | 0 |
| AIR | 1 | 0 | 1 | 0 | 0 |
| ELECTRONIC STABILITY CONTROL (ESC) | 1 | 0 | 0 | 1 | 0 |
| HYDRAULIC; AUTOHOLD BRAKE SYSTEM/BRAKE HOLD | 1 | 0 | 0 | 1 | 0 |
| PARKING BRAKE | 1 | 0 | 0 | 0 | 1 |
