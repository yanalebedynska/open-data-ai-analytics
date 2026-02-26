# REPORT

Лабораторна робота №1  
Open Data AI Analytics  
Студентка: Лебединська Яна
Група: ШІ-31

---

**Мета роботи**: Ознайомитися з роботою з Git та GitHub, навчитися працювати з гілками (feature branches), створювати Pull Request, вирішувати merge-конфлікти, організовувати структуру Python-проєкту та створювати реліз із тегом.

---

## 1. Створення репозиторію та ініціалізація Git-проєкту

### 1.1 Створення репозиторію на GitHub

На GitHub було створено новий публічний репозиторій `open-data-ai-analytics`.

<img width="1004" height="466" alt="image" src="https://github.com/user-attachments/assets/e7985ff4-482d-4127-9fff-fd57f61b39ef" />


---

### 1.2 Створення локальної папки проєкту

У каталозі з лабораторною роботою було створено папку `open-data-ai-analytics` та виконано перехід у неї.

Використані команди:
- cd /i/"3 курс/2 семестр/Середовище та компоненти розробки/Lab1"
- mkdir open-data-ai-analytics
- cd open-data-ai-analytics

<img width="1534" height="315" alt="image" src="https://github.com/user-attachments/assets/6652d9ab-0ea7-47b2-a82a-8822ff16ccf7" />

---

### 1.3 Ініціалізація Git-репозиторію

У створеній папці було ініціалізовано Git-репозиторій командою:
- git init

Після цього перевірено стан репозиторію:
- git status

<img width="1536" height="259" alt="image" src="https://github.com/user-attachments/assets/3dbcbe2e-762a-4bd1-8fe9-583b289b2d49" />

---

### 1.4 Підключення віддаленого репозиторію

Було додано віддалений репозиторій GitHub:
- git remote add origin https://github.com/yanalebedynska/open-data-ai-analytics

Перевірено правильність підключення:
- git remote -v

<img width="1004" height="119" alt="image" src="https://github.com/user-attachments/assets/eaf35faa-d1c7-4879-9a1c-3656266f8840" />

---

## 2. Додавання структури проєкту

На цьому етапі було створено базову структуру Python-проєкту відповідно до вимог лабораторної роботи.

### 2.1 Створення папок і службових файлів

Було створено необхідні каталоги та файли:

- `README.md`
- `.gitignore`
- `data/README.md`
- `notebooks/`
- `src/`
- `reports/figures/`

Використані команди:
- mkdir -p data notebooks src reports/figures
- touch README.md .gitignore data/README.md

<img width="1246" height="72" alt="image" src="https://github.com/user-attachments/assets/09095a60-326d-4011-97fd-789fe02d1595" />

---

### 2.2 Перевірка створеної структури

Для перевірки було використано команду `ls`, яка підтвердила наявність створених папок та файлів.

<img width="1249" height="69" alt="image" src="https://github.com/user-attachments/assets/028ff0cc-b682-4e28-acdb-ea9dd2bb837e" />

---

### 2.3 Додавання файлів до Git

Створені файли було додано до staging area та перевірено їх статус:
- git add .
- git status

<img width="1004" height="251" alt="image" src="https://github.com/user-attachments/assets/57c53c40-d2a7-4b3b-801c-97cd130b6e1c" />

---

### 2.4 Створення першого коміту

Було створено коміт зі структурою проєкту:
- git commit -m "add project structure (step 2)"

<img width="1004" height="127" alt="image" src="https://github.com/user-attachments/assets/ef2bcbbb-66a8-45ab-92b1-0ca2f6f696b0" />

---

### 2.5 Перейменування гілки та відправлення на GitHub

Гілку `master` було перейменовано на `main`, після чого виконано push до віддаленого репозиторію:
- git branch -M main
- git push -u origin main

<img width="1004" height="96" alt="image" src="https://github.com/user-attachments/assets/6a6d512e-8bac-4f59-a929-dcc092a91612" />
<img width="1004" height="204" alt="image" src="https://github.com/user-attachments/assets/92203e49-df4e-4a0d-aa0a-0375070a6ff4" />

---

### 2.6 Перевірка структури на GitHub

Після виконання push структура проєкту з’явилась у віддаленому репозиторії GitHub.

<img width="1004" height="407" alt="image" src="https://github.com/user-attachments/assets/03946378-eef3-4001-b2da-3d24f4fcc80b" />

---

## 3. Налаштування .gitignore

### 3.1 Додавання правил ігнорування

Було налаштовано файл `.gitignore` для виключення службових і тимчасових файлів з репозиторію.

До файлу додано:

- `__pycache__/` - кеш Python
- `.ipynb_checkpoints/` - службові файли Jupyter
- `.venv/`, `.env` - віртуальне середовище
- `data/raw/` - папка з сирими (великими) даними

Використана команда:
cat > .gitignore << 'EOF'
pycache/
.ipynb_checkpoints/

.venv/
.env

data/raw/
EOF

<img width="1343" height="218" alt="image" src="https://github.com/user-attachments/assets/c62117a2-4fc6-4669-ad60-906a1f240e45" />

---

### 3.2 Перевірка змін

Після редагування перевірено стан репозиторію:
- git status

Було видно, що файл `.gitignore` змінений.

<img width="1344" height="244" alt="image" src="https://github.com/user-attachments/assets/88bb491e-b87d-47be-8137-8fa2350e8de8" />

---

### 3.3 Додавання до staging та коміт

Файл додано до staging area та створено коміт:
- git add .gitignore
- git commit -m "chore: configure gitignore (step 3)"

<img width="1347" height="221" alt="image" src="https://github.com/user-attachments/assets/a0f1a6a2-1ba9-49e8-bbe5-4f8055857cb5" />
<img width="1004" height="75" alt="image" src="https://github.com/user-attachments/assets/d2285be1-a4f6-4c34-9329-29999dfbf54a" />

---

### 3.4 Відправлення змін на GitHub

Після коміту зміни було відправлено у віддалений репозиторій:
- git push origin main

<img width="1004" height="169" alt="image" src="https://github.com/user-attachments/assets/6b26c71a-e3f2-408a-9fda-0b4bc5595f4c" />

---

## 4. Заповнення README.md

### 4.1 Додавання опису проєкту

У файл `README.md` було додано:

- назву проєкту;
- мету лабораторної роботи;
- посилання на набір відкритих даних;
- 3 гіпотези для аналізу;
- короткий опис модулів та структури репозиторію.

<img width="1004" height="471" alt="image" src="https://github.com/user-attachments/assets/e36fc44e-d689-49e0-b016-2b86aef8f466" />

---

### 4.2 Додавання змін до Git

Після редагування файлу було перевірено стан репозиторію та додано `README.md` до staging area:
- git status
- git add README.md

<img width="1004" height="337" alt="image" src="https://github.com/user-attachments/assets/50028493-d85c-4490-ada9-445034408d97" />

---

### 4.3 Створення коміту

Було створено коміт із описом змін:
- git commit -m "docs: write README with dataset and hypotheses (step 4)"

<img width="1004" height="81" alt="image" src="https://github.com/user-attachments/assets/6bdd02eb-3da5-4598-a94d-f35f456ace44" />

---

### 4.4 Відправлення на GitHub

Після коміту зміни було відправлено до віддаленого репозиторію:
- git push origin main

<img width="1004" height="169" alt="image" src="https://github.com/user-attachments/assets/f88bc4ed-7697-4630-b52f-7221853e3941" />

---

## 5. Створення гілки feature/data_load та додавання скрипта завантаження даних

### 5.1 Створення нової гілки

Для реалізації модуля завантаження даних було створено окрему feature-гілку:
- git checkout -b feature/data_load

<img width="1004" height="109" alt="image" src="https://github.com/user-attachments/assets/ac715d30-f990-42c5-89f0-66113a8db1ba" />

---

### 5.2 Додавання скрипта data_load.py

У папці `src/` створено файл `data_load.py`, який:

- приймає локальний CSV-файл;
- зберігає дані у `data/raw/`;
- автоматично створює папку `data/raw/`, якщо її немає;
- підтримує аргументи командного рядка через `argparse`.

Основна функція:  
`load_data()` - завантажує або копіює файл у `data/raw/`.

<img width="1004" height="72" alt="image" src="https://github.com/user-attachments/assets/a93db0da-66d0-44b1-856e-e994256d250d" />

---

### 5.3 Додавання файлу до Git

Перевірено статус та додано новий файл до staging area:
- git status
- git add src/data_load.py

<img width="1004" height="224" alt="image" src="https://github.com/user-attachments/assets/61c182a1-9928-4008-bafa-8f2751ccbb9c" />

---

### 5.4 Створення коміту

Створено коміт із описом змін:
- git commit -m "feat: add data loading script (data_load)"

<img width="1004" height="96" alt="image" src="https://github.com/user-attachments/assets/8912c067-8150-4893-b145-fcbc95d2dde5" />

---

### 5.5 Відправлення гілки на GitHub

Гілку було відправлено у віддалений репозиторій:
- git push -u origin feature/data_load

<img width="1004" height="254" alt="image" src="https://github.com/user-attachments/assets/48492370-2401-47cb-8533-71b1f3b5c633" />

---

## 6. Злиття гілки feature/data_load у main

### 6.1 Створення Pull Request

<img width="1004" height="639" alt="image" src="https://github.com/user-attachments/assets/3319415b-abd1-45f6-aa34-63f4c4688b1a" />

---

### 6.2 Перевірка відсутності конфліктів

GitHub показав, що конфлікти відсутні  
(`Able to merge - No conflicts with base branch`).

<img width="1004" height="638" alt="image" src="https://github.com/user-attachments/assets/e6924f0c-67da-40a4-9b2b-1ec08978dfc5" />

---


### 6.3 Merge Pull Request

Було виконано злиття гілки через кнопку **Merge pull request**.

Після цього:
- PR отримав статус **Merged**
- зміни інтегровані у `main`

<img width="1004" height="655" alt="image" src="https://github.com/user-attachments/assets/0de749dc-6848-448d-a92e-8ab6c9d66144" />


---

### 6.4 Перевірка результату

Після злиття файл `src/data_load.py` відображається у гілці `main`.

<img width="1004" height="473" alt="image" src="https://github.com/user-attachments/assets/1cfe3e5a-a300-4ef8-847c-81a33ff3d9d2" />

---

## 7. Створити 2 feature-гілки (data_quality_analysis + data_research)

### 7.A Гілка `feature/data_quality_analysis` — модуль перевірки якості даних

**7.1 Створення гілки**
- Створила гілку та перейшла в неї:
  - `git checkout -b feature/data_quality_analysis`
  - `git branch` (перевірила, що активна саме ця гілка)
 
<img width="1004" height="315" alt="image" src="https://github.com/user-attachments/assets/1b839fac-075c-4d49-9edc-1534bc185e44" />
<img width="1004" height="161" alt="image" src="https://github.com/user-attachments/assets/fac13a60-b003-4867-8039-7e2df3109f54" />

---

**7.2 Перевірка роботи скрипта**
- Запустила модуль якості даних на завантаженому датасеті:
  - `py src/data_quality_analysis.py --input data/raw/dtp_2015.csv`
- Скрипт згенерував звіт `reports/quality_report.json` і вивів коротку статистику (Rows/Columns/Duplicates).

<img width="1004" height="81" alt="image" src="https://github.com/user-attachments/assets/01b6cee4-1370-4b83-a6d0-2e9342d23ce3" />

---

**7.3 Коміт і push гілки**
- Зафіксувала код модуля:
  - `git add src/data_quality_analysis.py`
  - `git commit -m "feat: add data quality analysis module"`
- Відправила гілку на GitHub:
  - `git push -u origin feature/data_quality_analysis`

<img width="1004" height="294" alt="image" src="https://github.com/user-attachments/assets/e4035da5-7d58-4acc-a2ad-98bfcba78804" />

---

### 7.B Гілка `feature/data_research` - модуль дослідження/аналізу даних

**7.4 Повернення на main і створення гілки**
- Повернулась на `main` і підтягнула останні зміни:
  - `git checkout main`
  - `git pull origin main`
- Створила гілку і перейшла в неї:
  - `git checkout -b feature/data_research`
  - `git branch` (перевірила активну гілку)

<img width="1004" height="293" alt="image" src="https://github.com/user-attachments/assets/6fce0796-f295-41a4-949a-a5e1dc79d17e" />

---

**7.5 Перевірка роботи скрипта**
- Запустила модуль дослідження на датасеті:
  - `py src/data_research.py --input data/raw/dtp_2015.csv`
- Скрипт зберіг результат у `reports/research_summary.json` і вивів базову статистику (Rows/Columns).

<img width="1004" height="87" alt="image" src="https://github.com/user-attachments/assets/b8f60b26-05b5-428d-a0fd-fc306aa96a60" />

---

**7.6 Коміт і push гілки**
- Зафіксувала код модуля:
  - `git add src/data_research.py`
  - `git commit -m "feat: add data research module"`
- Відправила гілку на GitHub:
  - `git push -u origin feature/data_research`

  <img width="1004" height="96" alt="image" src="https://github.com/user-attachments/assets/69de10a4-2415-458d-ace6-018a8dd928e1" />
  <img width="1004" height="257" alt="image" src="https://github.com/user-attachments/assets/b0eb708b-8e8c-43a9-a371-e24f47df8630" />

---

## 8. Злиття feature-гілок у main через Pull Request

### 8.1 Merge гілки feature/data_quality_analysis

Було створено Pull Request для злиття `feature/data_quality_analysis` у `main`.

<img width="1004" height="464" alt="image" src="https://github.com/user-attachments/assets/32a4f2db-6739-4fe6-a08f-f36b9fee58aa" />

---

#### Після перевірки відсутності конфліктів (`Able to merge`) виконано **Merge pull request**.

<img width="1004" height="625" alt="image" src="https://github.com/user-attachments/assets/adb9d6aa-2c0c-434f-a0cc-2c48748fef51" />
<img width="1004" height="137" alt="image" src="https://github.com/user-attachments/assets/bf0f735c-abbe-4da6-9041-206472a58669" />

---

### 8.2 Merge гілки feature/data_research

Аналогічно створено Pull Request для гілки `feature/data_research`.

<img width="1004" height="477" alt="image" src="https://github.com/user-attachments/assets/148dffeb-86cf-435d-8de8-cbcbb33ff894" />

#### Після перевірки відсутності конфліктів виконано злиття.

<img width="1004" height="549" alt="image" src="https://github.com/user-attachments/assets/9b2bf631-e509-4ff4-b5c6-868a4df6d191" />
<img width="1004" height="124" alt="image" src="https://github.com/user-attachments/assets/a8c19808-931a-4bc4-a8ba-2ac3e58a1714" />

---

### 8.3 Перевірка результату

Після злиття обидва файли відображаються у гілці `main`:

- `src/data_quality_analysis.py`
- `src/data_research.py`

<img width="1004" height="305" alt="image" src="https://github.com/user-attachments/assets/90798c87-9c9a-4d57-8679-92cffc72d5a2" />

---

### 8.4 Оновлення локальної гілки main після merge

Після злиття обох feature-гілок на GitHub було оновлено локальну гілку `main`:

<img width="1004" height="354" alt="image" src="https://github.com/user-attachments/assets/8e55a818-097b-4d25-ac0c-2e2114357dc7" />

---

## 9. Створення та розв’язання merge-конфлікту в README.md

### 9.1 Створення гілки conflict/readme-a

Створено гілку:
- git checkout -b conflict/readme-a

<img width="1004" height="152" alt="image" src="https://github.com/user-attachments/assets/cb0472ee-177d-44b6-bf3a-b5a48f3ef9c1" />

---

### 9.1.1 Змінюю одну секцію README.md

У секції **“Питання / гіпотези для аналізу”** змінено 1-й пункт.

Було:
> “Сезонність: кількість ДТП протягом року нерівномірна...”

Стало:
> “Сезонність (A): найбільше ДТП очікується восени та взимку.”

Після цього виконано коміт та push.

<img width="1004" height="310" alt="image" src="https://github.com/user-attachments/assets/d9996451-b7a3-4a2b-a85c-b9b2f1fa6993" />

---

### 9.2 Створення гілки conflict/readme-b

Повертаюсь у main та створюю нову гілку:
- git checkout main
- git checkout -b conflict/readme-b

<img width="1004" height="268" alt="image" src="https://github.com/user-attachments/assets/dc9e1751-b8f3-4df9-a655-f98a93a627f8" />

---

### 9.2.1 Змінюю ту саму секцію, але інакше

У тій самій частині README змінено той самий пункт, але з іншим формулюванням.

Стало:
> “Сезонність (B): найбільше ДТП очікується влітку через збільшення трафіку.”

Після цього виконано коміт та push.

<img width="1004" height="315" alt="image" src="https://github.com/user-attachments/assets/75e40b66-6625-42fd-b96c-ed244358fc87" />

---

## 9.3 Виникнення merge-конфлікту

Гілка conflict/readme-a була успішно змерджена у main.

Під час спроби змерджити conflict/readme-b виник конфлікт, оскільки:
- обидві гілки змінили один і той самий рядок
- Git не зміг автоматично визначити правильну версію

<img width="1004" height="230" alt="image" src="https://github.com/user-attachments/assets/984281f9-c4de-40c9-8472-6b7c8815d678" />
<img width="1004" height="198" alt="image" src="https://github.com/user-attachments/assets/633cb261-0a0f-40a7-80ba-372caba1fb57" />

---

## 9.4 Вирішення merge-конфлікту

<img width="1004" height="464" alt="image" src="https://github.com/user-attachments/assets/0f0448f5-5a10-414a-9a22-fbb0d465d7b3" />
<img width="1004" height="135" alt="image" src="https://github.com/user-attachments/assets/d929f525-85dc-48ff-a8c6-943bb89a4332" />

---

## 10. Створення гілки feature/visualization та додавання коду візуалізації

### 10.1 Створення гілки feature/visualization

Після оновлення `main` створено нову feature-гілку:
- git checkout -b feature/visualization

Гілка створена від актуального `main`, щоб ізольовано додати модуль побудови графіків.

<img width="1004" height="179" alt="image" src="https://github.com/user-attachments/assets/72ba2d03-ba8f-4918-941b-03ad33c6f55d" />

---

### 10.2 Додавання модуля візуалізації

У файлі `src/visualization.py` реалізовано:
- зчитування CSV-файлу з `data/raw/`
- побудову графіка (топ-10 значень першої колонки)
- збереження результату у `reports/figures/`

Скрипт було запущено: 
- py src/visualization.py --input data/raw/dtp_2015.csv

У результаті створено файл: reports/figures/top10_first_column.png

<img width="1004" height="121" alt="image" src="https://github.com/user-attachments/assets/0dee16a3-f589-48bb-978d-a6092a24f136" />
<img width="1004" height="67" alt="image" src="https://github.com/user-attachments/assets/72ef465f-1fed-455f-977e-2f1aba7e0e64" />

---

### 10.3 Коміт та push гілки

Після перевірки роботи скрипта виконано коміт та push:
- git commit -m "feat: add visualization module"
- git push -u origin feature/visualization

<img width="1004" height="283" alt="image" src="https://github.com/user-attachments/assets/41ebef61-0ea4-45df-b9ba-893cc67b8264" />

---

### 10.4 Merge через Pull Request

На GitHub створено Pull Request з `feature/visualization` у `main`.

<img width="1004" height="646" alt="image" src="https://github.com/user-attachments/assets/2353b07d-bb6d-417b-af9e-3509c62e6d83" />
<img width="1004" height="123" alt="image" src="https://github.com/user-attachments/assets/8a79009a-650b-414d-9e52-e11fcde6759c" />

---

## 11. Додавання CHANGELOG.md та створення тегу v0.1.0

### 11.1 Переходжу в main і оновлюю його

Перед створенням релізу перейшла у гілку `main` та переконалась, що вона актуальна:
- git checkout main
- git pull origin main

<img width="1004" height="396" alt="image" src="https://github.com/user-attachments/assets/76bb7058-bc0a-486c-a76c-ef46c5b64eea" />

---

### 11.2 Створюю файл CHANGELOG.md

Створено файл `CHANGELOG.md`, у якому описано реліз **v0.1.0**.

У CHANGELOG зазначено:
- створення структури проєкту
- додавання модулів `data_load`, `data_quality_analysis`, `data_research`, `visualization`
- демонстрацію merge-конфлікту та його розв’язання

<img width="1004" height="385" alt="image" src="https://github.com/user-attachments/assets/697236bc-9bb0-4871-82d3-e23195adeb92" />

---

### 11.3 Додаю CHANGELOG у Git

Файл було додано до staging area:
- git add CHANGELOG.md
- git status

<img width="1004" height="273" alt="image" src="https://github.com/user-attachments/assets/ce132d54-7e16-4ee8-8c78-1783f8ba5d9d" />

---

### 11.4 Роблю коміт

Після цього створено коміт:
- git commit -m "docs: add CHANGELOG for v0.1.0"

<img width="1004" height="109" alt="image" src="https://github.com/user-attachments/assets/37bbcf48-a0b9-49f0-a5b4-7f19c588cc47" />

---

### 11.5 Пушу зміни в main

Запушила зміни до віддаленого репозиторію:
- git push origin main

<img width="1004" height="205" alt="image" src="https://github.com/user-attachments/assets/e32ce662-d895-46e9-95c0-cc88f08b2b82" />

---

### 11.6 Створюю тег v0.1.0

Після цього створено релізний тег:
- git tag v0.1.0

Перевірила, що тег створився:
- git tag

<img width="1004" height="153" alt="image" src="https://github.com/user-attachments/assets/adfead5c-24a2-441e-859c-8e90f60f01fa" />

---

### 11.7 Пушу тег на GitHub

Опублікувала тег у віддаленому репозиторії:
- git push origin v0.1.0

<img width="1004" height="113" alt="image" src="https://github.com/user-attachments/assets/61266ca2-75c5-4cde-ab80-e8a47224d801" />

---

## 12. Перевірка створеного релізу на GitHub

Після створення та пушу тегу `v0.1.0` я перевірила його на GitHub у вкладці **Tags / Releases**.

Було підтверджено, що:
- тег `v0.1.0` присутній у репозиторії
- він прив’язаний до останнього коміту в гілці `main`
- реліз відображається у списку тегів


<img width="1004" height="280" alt="image" src="https://github.com/user-attachments/assets/13b87109-226c-4aa1-941d-53db5189fa68" />

---

## 13. Git-історія проєкту

Для перегляду структури гілок та історії комітів було використано команду:
- git --no-pager log --oneline --graph --decorate --all

Що показує ця команда:

--oneline - скорочений вигляд комітів (hash + повідомлення)
--graph - візуальне дерево гілок
--decorate - показує, де знаходяться гілки та теги
--all - відображає всі гілки

<img width="1004" height="612" alt="image" src="https://github.com/user-attachments/assets/ec97fab4-fed4-4d24-b286-a4fddae31c9a" />


## Висновок

У межах лабораторної роботи було:

- створено структуру проєкту
- реалізовано 4 модулі (`data_load`, `data_quality_analysis`, `data_research`, `visualization`)
- продемонстровано роботу з feature-гілками
- створено та коректно розв’язано merge-конфлікт
- оформлено CHANGELOG
- створено релізний тег `v0.1.0`
