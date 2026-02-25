<img width="1344" height="244" alt="image" src="https://github.com/user-attachments/assets/fb9d7c47-6277-4e96-928e-173028fdb083" /># REPORT

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
`cat > .gitignore << 'EOF'
pycache/
.ipynb_checkpoints/

.venv/
.env

data/raw/
EOF`

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




