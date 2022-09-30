from django.http import HttpResponse

def Welcome(request):
    return HttpResponse("<h1> Good Day! Welcome to CCMS Department! <h1/>")

def Mission(request):
    return HttpResponse(" <p> MISSION <p/>  The College of Computing and Multimedia Studies shall produce competent and innovative professionals or Technopreneurs in the Information and Communication Technology (ICT) industry adequately prepared in the practice of their profession supportive of national development goals and standards of global excellence." )

def Vision(request):
    return HttpResponse("<p> VISION <p/> The College of Computing and Multimedia Studies shall be a center of excellence in delivering Computing and Multimedia education")

def Objectives(request):
    return HttpResponse("""<p> CCMS PROGRAM EDUCATIONAL OBJECTIVES 
    <p> After graduation, alumni of MSEUF CCMS programs shall: <p/>
    <p> 1. Be employed and demonstrate professionalism, competence, and passion in solving contemporary computing problems by developing or utilizing inovative IT solutions; ")
    <p> 2. In lifelong learning or research to attune to the continous innovation in the IT industry in order to adapt to the changing demand of the global market; and
    <p> 3. Exhibit leadership and teamwork, and commitment to their respective local or global organization <p/> """)
