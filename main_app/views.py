import datetime

from django.shortcuts import render, redirect

from main_app.app_forms import ReportForm


# Create your views here.
def home(request):
    date_in_yrs = datetime.datetime.now()
    reports = {
        "Bomet County Opinion Poll Release": {
            "filename": "counties/PUBLIC OPINION {BOMET COUNTY}.pdf",
            "release_date": "January 2024"
        },
        "Kakamega County Opinion Poll Release": {
            "filename": "counties/PUBLIC OPINION {KAKAMEGA COUNTY}-3_240131_170941.pdf",
            "release_date": "January 2024"
        },
        "Isiolo County Opinion Poll Release": {
            "filename": "counties/PUBLIC OPINION {ISIOLO COUNTY}.pdf",
            "release_date": "January 2024"
        },
        "Nyeri County Opinion Poll Release": {
            "filename": "counties/PUBLIC OPINION {NYERI COUNTY}.pdf",
            "release_date": "January 2024"
        },
        "Kirinyaga County Opinion Poll Release": {
            "filename": "counties/PUBLIC OPINION {KIRINYAGA COUNTY}.pdf",
            "release_date": "January 2024"
        },
        "Samburu County Opinion Poll Release": {
            "filename": "counties/PUBLIC OPINION {SAMBURU COUNTY}.pdf",
            "release_date": "January 2024"
        },
        "Top Impactful Members of Parliament": {
            "filename": "POLITRACK MPS  SURVEY DEC 10.pdf",
            "release_date": "December 2023"
        },
        "Top 20 Impactful Governors": {
            "filename": "POLITRACK GOVERNOR SURVEY TOP 20.pdf",
            "release_date": "November 2023"
        },
        "Top 20 Senators Approval Rating": {
            "filename": "POLITRACK SENATOR SURVEY presentation.pdf",
            "release_date": "October 2023"
        },
        "Top 50 MP Approval Rating": {
            "filename": "POLITRACK MPS SURVEY for presentation with regions.pdf",
            "release_date": "October 2023"
        },
        "Government preparedness for El Nino": {
            "filename": "GOVERNMENT PREPARDNESS FOR EL-NINO RAINS.pdf",
            "release_date": "October 2023"
        },
        "Governors Approval Rating (1yr in Office)": {
            "filename": "POLITRACK AFRICA SURVEY.pdf",
            "release_date": "September 2023"
        },
        "Top 20 Governors Performance Ranking": {
            "filename": "POLITRACK GORVERNOR SURVEY LIST.pdf",
            "release_date": "September 2023"
        },
        "Top 20 MP Performance Ranking": {
            "filename": "TOP 20 MP'S PERFORMANCE RANKING.pdf",
            "release_date": "May 2023"
        }
    }

    data = {
        "date": date_in_yrs.year,
        "reports": reports
    }

    return render(request, template_name="index.html", context=data)


def item(request):
    return render(request, 'inner-page.html')


def portfolio(request):
    return render(request, 'portfolio-details.html')


def alt_home(request):
    return render(request, 'untouched_index.html')


def form(request):
    if request.method == 'POST':
        my_form = ReportForm(request.POST)
        if my_form.is_valid():
            my_form.save()
            return redirect('alt_home')

    my_form = ReportForm()

    return render(request, 'form.html', {'form': my_form})
