from django.shortcuts import render
from pathlib import Path
from PersonalWebsite.models import CodeProject, ArtProject, Certificate, Testimonial, Skill, TimelineEntry, PersonalDescription


header_links = [
    {"name": "Home",
     "url": "/"},
    {"name": "Code",
     "url": "/code"},
    {"name": "Art",
     "url": "/art"},
    {"name": "Text",
     "url": "/text"}
     ]

data_dict = {
    'header_links': header_links,
    'testimonials': Testimonial.objects.all(),
    'code_projects': CodeProject.objects.all(),
    'art_projects': ArtProject.objects.all(),
    'certificates': Certificate.objects.all(),
    'skills': Skill.objects.all(),
    'personal_description': PersonalDescription.objects.last(),
}

def render_portfolio(language):
    """
    Render the template in template with data from data.

    param:
        - language
    """
    file_loader = FileSystemLoader('templates')
    env = Environment(loader=file_loader)
    if language == "en":
        for head_link in header_links:
            templ = head_link["url"]
            template = env.get_template(templ)
            rendered = template.render(**data_dict, current_page=templ)

            with open(templ, 'w') as file:
                file.write(rendered)
            print(f"Rendered {templ}")

    if language == "sv":
        #TODO replace all texts to swedish
        print("TODO: Svenska är inte implementerat")
        fodler = "sve/"
        for head_link in header_links:
            templ = head_link["url"]
            template = env.get_template(templ)
            for data_key, data in data_dict.items():
                for data_item in data:
                    if 'title' in data_item and 'title_sv' in data_item:
                        data_item['title'] = data_item['title_sv']
                    if 'description' in data_item and 'description_sv' in data_item:
                        data_item['description'] = data_item['description_sv']
        
            rendered = template.render(lang = 'sve', **data_dict, current_page=templ)

            with open(fodler+templ, 'w') as file:
                file.write(rendered)

            print(f"Rendered {templ}")


if __name__ == '__main__':
    print("Rendering Web Pages...")
    render_portfolio("en")
    render_portfolio("sv")

def index(request):
    print(data_dict['code_projects'])
    return render(request, 'index.html', data_dict)

def code_page(request):
    return render(request, 'code_page.html', data_dict)

def art_page(request):
    return render(request, 'art_page.html', data_dict)

def timeline(request):
    return render(request, 'timeline.html', data_dict)

def text_page(request):
    return render(request, 'text_page.html', data_dict)