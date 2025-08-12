from jinja2 import Environment, FileSystemLoader
from pathlib import Path

# Dummy data mimicking your Property objects (simplified dicts)
dummy_properties = [
    {
        "uprn": "1001",
        "address": "30 Alexandra Road, Muswell Hill, N10 2RT",
        "lat": 51.406,
        "long": -0.372,
        "score": 3,
    },
    {
        "uprn": "1002",
        "address": "",
        "lat": None,
        "long": None,
        "score": 2,
    },
]

def fake_url_for(endpoint, **values):
    # A simple stub for url_for, you can extend if needed
    if endpoint == "property":
        return f"/{values.get('uprn', '')}"
    return "/"

def test_home_template_renders():
    # Point to the directory where your templates live
    templates_dir = Path(__file__).parent.parent / "templates"
    env = Environment(loader=FileSystemLoader(str(templates_dir)))
    
    # Inject a fake url_for into the template globals (needed by your template)
    env.globals["url_for"] = fake_url_for
    
    template = env.get_template("home.html")
    
    rendered_html = template.render(properties=dummy_properties, key="dummykey")
    
    # Basic assertions to check key content is rendered
    assert "Hard to Heat Homes" in rendered_html
    assert "30 Alexandra Road" in rendered_html
    assert 'id="1001"' in rendered_html  # uprn used in id
    assert 'id="1002"' in rendered_html  # second property
    assert "Click for address" in rendered_html  # address missing case
    assert "51.406" in rendered_html
 


