from django.shortcuts import render, redirect
from .forms import MadLibForm
from .models import MadLibResponse

def home(request):
    return render(request, 'madlib_question.html')  # ✅ Render a homepage

def madlib_question(request, step=1):
    fields = [
        ("adjective1", "Enter an adjective"), 
        ("software_type", "Enter a type of software"), 
        ("programming_language", "Enter a programming language"), 
        ("number", "Enter a number"), 
        ("bug_type", "Enter a type of bug"), 
        ("adjective2", "Enter another adjective"), 
        ("verb_ing", "Enter a verb ending in -ing"), 
        ("plural_noun", "Enter a plural noun"), 
        ("software_company", "Enter a famous software company"), 
        ("silly_word", "Enter a silly word"), 
        ("verb_past", "Enter a verb (past tense)"), 
        ("famous_person", "Enter a famous person"), 
        ("adjective3", "Enter another adjective"), 
        ("noun1", "Enter a noun"), 
        ("verb1", "Enter a verb"), 
        ("verb2", "Enter another verb"), 
        ("adjective4", "Enter another adjective"), 
        ("noun2", "Enter another noun")
    ]

    if step > len(fields):
        return redirect('madlib_result')

    field_name, question_text = fields[step - 1]
    
    if request.method == "POST":
        request.session[field_name] = request.POST.get(field_name)
        return redirect('madlib_question', step=step + 1)

    return render(request, 'madlib_question.html', {
        "field_name": field_name, 
        "question_text": question_text, 
        "step": step
    })

def madlib_result(request):
    story = f"""
    Once upon a time, in a {request.session.get('adjective1', 'fantastic')} world of software development, 
    there was a {request.session.get('software_type', 'app')} that was written in {request.session.get('programming_language', 'Python')}. 
    The developers had only {request.session.get('number', '10')} days to get rid of the {request.session.get('bug_type', 'glitch')} that kept popping up. 
    It was a {request.session.get('adjective2', 'tough')} task, but by {request.session.get('verb_ing', 'debugging')} their {request.session.get('plural_noun', 'codes')}, 
    they managed to catch the attention of {request.session.get('software_company', 'Google')}.

    "Wow, this code is so {request.session.get('silly_word', 'blorp')}!" exclaimed the CEO of {request.session.get('software_company', 'Google')}. 
    They {request.session.get('verb_past', 'decided')} to hire the team on the spot. 
    {request.session.get('famous_person', 'Elon Musk')} even called them {request.session.get('adjective3', 'brilliant')} 
    and gave them a {request.session.get('noun1', 'trophy')} as a token of appreciation.

    In the end, the developers learned to always {request.session.get('verb1', 'test')} before they {request.session.get('verb2', 'deploy')}. 
    It was a {request.session.get('adjective4', 'valuable')} lesson that they would carry with them to their next project, 
    along with their trusty {request.session.get('noun2', 'laptop')}.
    """
    
    return render(request, 'madlib_result.html', {"story": story})
