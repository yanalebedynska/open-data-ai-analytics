import json
from pathlib import Path

from flask import Flask, render_template, send_from_directory


app = Flask(__name__)

REPORTS_DIR = Path("/app/reports")
PLOTS_DIR = Path("/app/plots")


def load_json_file(path: Path):
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


@app.route("/")
def index():
    load_report = load_json_file(REPORTS_DIR / "load_report.json")
    quality_report = load_json_file(REPORTS_DIR / "quality_report.json")
    research_report = load_json_file(REPORTS_DIR / "research_summary.json")

    plot_files = sorted([p.name for p in PLOTS_DIR.glob("*.png")])

    summary_cards = []

    if load_report:
        summary_cards.append({
            "title": "Завантажено рядків",
            "value": load_report.get("rows_loaded", "—")
        })
        summary_cards.append({
            "title": "Кількість стовпців",
            "value": load_report.get("columns_loaded", "—")
        })

    if quality_report:
        summary_cards.append({
            "title": "Пропущені значення",
            "value": quality_report.get("missing_values_total", "—")
        })
        summary_cards.append({
            "title": "Дублікати",
            "value": quality_report.get("duplicate_rows", "—")
        })

    return render_template(
        "index.html",
        load_report=load_report,
        quality_report=quality_report,
        research_report=research_report,
        plot_files=plot_files,
        summary_cards=summary_cards,
    )


@app.route("/plots/<path:filename>")
def serve_plot(filename):
    return send_from_directory(PLOTS_DIR, filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)