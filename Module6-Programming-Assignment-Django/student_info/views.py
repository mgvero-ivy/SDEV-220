from django.shortcuts import redirect, render


def student_form(request): #displays the blank input form
    return render(request, "student_info/student_form.html")


def student_results(request):   #gets the data from the form and passes it to the results page
    

    if request.method != "POST":
        return redirect("student_form") 

    student_name = request.POST.get("student_name", "").strip()
    student_id = request.POST.get("student_id", "").strip()

    if not student_name or not student_id:  #returns an error if either name or id is left blank
        return render(
            request,
            "student_info/student_form.html",
            {
                "error": "Student Name and Student ID are required.",
                "form_data": request.POST,
            },
        )

    student = {     #collects the data from the form and stores it in an array
        "name": student_name,
        "student_id": student_id,
        "major": request.POST.get("major", ""),
        "class_standing": request.POST.get("class_standing", ""),
        "languages": request.POST.getlist("languages"),
        "graduation_year": request.POST.get("graduation_year", ""),
        "comments": request.POST.get("comments", ""),
    }

    return render(      #directs to student_results.html
        request,
        "student_info/student_results.html",
        {"student": student},
    )