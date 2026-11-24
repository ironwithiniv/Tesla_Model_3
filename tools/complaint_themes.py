"""Count NHTSA complaint themes by keyword. usage: python3 tools/complaint_themes.py NHTSA/raw"""
import json, re, sys, collections

RAW = sys.argv[1]
PATS = {
    'phantom/false braking': r'phantom brak|false brak|braked suddenly|sudden(ly)? brak|ghost brak',
    'upper control arm/ball joint': r'upper control arm|control arm|ball joint|FUCA',
    'suspension clunk/creak': r'clunk|creak',
    'screen black/MCU': r'screen (went|goes|turn(ed|s)?) black|black screen|touchscreen (fail|froze|reboot|went)|display (fail|went black)|MCU|emmc',
    'heat pump/HVAC fail': r'heat pump|no heat|cabin heat|a/c (stop|fail)|air condition(ing)? (stop|fail)|hvac',
    '12V/LV battery': r'12v|12 v |low voltage battery|lv battery|16v',
    'HV battery/range loss': r'battery (fail|degrad)|range (loss|drop|decreas)|reduced range|hv battery|high voltage battery',
    'drive unit/motor': r'drive unit|motor (fail|noise)|whine|reduced power|power reduced',
    'water leak/trunk': r'water (leak|in the trunk|ingress)|leak(s|ed|ing)? .*trunk|trunk .*water',
    'loss of steering assist': r'steering assist|power steering',
    'seat belt/airbag': r'airbag|air bag|seat belt',
}
for y in (2021, 2022, 2023, 2024):
    cs = json.load(open(f'{RAW}/complaints_{y}.json'))['results']
    print(y, 'total', len(cs), {k: sum(1 for c in cs if re.search(p, c.get('summary') or '', re.I)) for k, p in PATS.items()})
