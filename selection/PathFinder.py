import webbrowser



#FOREIGN COLLEGES   #FOREIGN COLLEGES    #FOREIGN COLLEGES    #FOREIGN COLLEGES    #FOREIGN COLLEGES    #FOREIGN COLLEGESs="['accounting', 'marketing', 'finance', 'geological sciences', 'environment and resources', 'aeronautics and astronautics', 'bioengineering', 'electrical engineering', 'design', 'computational and mathematical', 'civil engineering', 'management science', 'applied physics', 'archeology', 'arts institue', 'biology', 'chemistry', 'economics', 'film production', 'mathematics', 'religious studies', 'law', 'architecture', 'aerospace', 'data science', 'computer science', 'history', 'literature', 'mechanical engineering', 'physics', 'nuclear science and engineering', 'neuro biology', 'social studies', 'classics', 'english', 'astrophysics', 'business management', 'pharmaceutical', 'biochemistry', 'french', 'german', 'spanish', 'geography', 'fine arts', 'chinese studies', 'japanese', 'malay studies', 'english literature', 'south east asian studies', 'east asian studies', 'comparative literature', 'agricultural science', 'animal science', 'astronomy', 'philosophy', 'nuclear science', 'african studies', 'american studies', 'anthropology', 'archaeology', 'russian', 'statistics', 'political science', 'Biological and Biomedical Sciences', 'Engineering and Electronics', 'Environmental and Ecological Sciences', 'Geography', 'Earth Sciences (Geology and Geophysics)','uban planning', 'business',  'chemical engineering', 'metallurgical engineering', 'automobile', 'Aerospace Engineering', 'Management Studies', ‘Applied Mechanics', 'Biotechnology', 'Engineering Design', 'Metallurgical and Materials Engineering', 'Humanities and Social Sciences', 'Ocean Engineering', 'Biological Sciences and Bio-Engineering', 'Materials Science and Engineering', 'Financial Accounting', 'Corporate Finance', 'Business, Government and Society', 'Managerial Communication-I', 'Managerial Communication-II', 'Macroeconomics', 'Marketing Management', 'Managing People and Performance in Organizations', 'Management Accounting', 'Managerial Economics', 'Operations Management', 'Organization Design', 'Competition & Strategy', 'Entrepreneurial Learning', 'Commerce', 'English', 'Hindi', 'Journalism', 'Philosophy', 'Political Science', 'Psychology', 'Sanskrit', 'Sociology', 'Statistics', 'sociology']"



def StanfordUniversity( ): #Stanford University 
    print('''Located in the heart of Silicon Valley, Stanford University was founded in 1885 by Jane and Leland Stanford, “to promote the public welfare by exercising an influence in behalf of humanity and civilization.” Since opening in 1891, Stanford's faculty and students have worked to improve the health and wellbeing of people around the world through the discovery and application of knowledge. Breakthroughs at Stanford include the first successful heart-lung transplant, the debut of the computer mouse, and the development of digital music.

Situated on 8,180 acres, Stanford is one of the largest campuses in the United States with 18 interdisciplinary research institutes and seven schools on a single campus: Graduate School of Business; School of Earth, Energy & Environmental Sciences; Graduate School of Education; School of Engineering; School of Humanities and Sciences; Law School; and School of Medicine.

Stanford has more than 16,300 students, 2,180 faculty and 1,800 postdoctoral scholars. Stanford is an international institution, enrolling students from all 50 U.S. states and more than 90 other countries. It is also an athletics powerhouse, with 900 current student-athletes and a history of 137 national championships and 23 consecutive Directors’ Cups, awarded to the top intercollegiate athletics program in the nation.

Stanford counts 19 Nobel laureates within its community today and numerous famous alumni associated with the university from the worlds of art, social sciences, business, politics, humanities, media, sports and technology. The 31st president of the US, Herbert Hoover, was part of the first class at Stanford, and received a degree in geology in 1895. The alumni include 17 astronauts, 18 Turing Award recipients and two Fields Medalists.

In total, companies founded by Stanford affiliates and alumni generate more than $2.7 trillion annual revenue, which would be the 10th largest economy in the world. These companies include Google, Nike, Netflix, Hewlett-Packard, Sun Microsystems, Instagram and Charles Schwab. Stanford alumni also have founded nonprofit organizations like Kiva and SIRUM. The first American woman to go into space, Sally Ride, received an undergraduate degree in physics from Stanford in 1973. Just 10 years later, she made her ascent into space.

Stanford’s official seal contains the German words, “Die Luft der Freiheit weht”, which translates as “the wind of freedom blows”.''')           
    ow="https://www.stanford.edu/"     # <- official website 
    al="https://admission.stanford.edu/" # <- admission link
    stat='https://www.topuniversities.com/universities/stanford-university#wurs'#<- link for complete stats on college
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])

def MIT ():# <- MIT
    print ('''Incorporated in the year 1861, Massachusetts Institute of Technology is a private research institute located in Cambridge, Massachusetts. In 1865, four years after the approval of its founding charter, the Institute admitted its first student and shortly thereafter in 1871, admitted its first woman student. MIT’s opening marked the foundation of a new kind of independent educational institution by coupling teaching and research with a primary focus on solving real-world problems. There are 30 departments across 5 schools in MIT, pioneering new ways of learning on the campus.

            With more than 1,067 Faculty members, MIT continues to play a vital role in shaping the future of undergraduate and graduate students as advisors, mentors, coaches, committee members and much more. In addition, the Institute’s board of trustees include 78 eminent leaders in science, engineering, education, industry, and other professions. Additionally, the faculty members continue to thrive the global standard of excellence in their disciplines.

            MIT is set in a campus of 168 acres, situated between Central and Kendall Squares, and across the Charles River from Boston’s Back Bay; comprising of 26 acres of playing fields, more than 20 gardens and green spaces, 18 student residences and around 50 publicly cited works of art.

            The academic departments and institutes encompass numerous degree-granting programs and interdisciplinary centers, laboratories, and programs. In the year 2019-20, MIT student population of 11,520 including 458 international undergraduate and 2873 international graduate students came from all 50 states, the District of Columbia, four territories, and 129 foreign countries. MIT also offers a number of executive and professional programs for entrepreneurs, executives, managers, and technical professionals through online as well as on-campus mode.  

            Many MIT staff are eminent international scholars from different parts of the world. MIT is placed at the heart of one of the most vibrant hubs of innovation and entrepreneurship – Cambridge. From medical research to clean water technology, sustainable energy, urban resiliency, Alzheimer’s, cancer and infectious disease are some of the innovations where MIT scholars have made an impact. In the academic year 2016–2017, MIT hosted 2,379 international scholars comprising of 75% men and 25% women from 96 countries. It is one of the top institutions that produced 95 Noble laureates, 59 National Medal of Science winners, 29 National Medal of Technology and Innovation winners, 77 MacArthur Fellows and 15 A. M. Turing Award winners.''')

        #Links
    stat='https://www.topuniversities.com/universities/massachusetts-institute-technology-mit#wurs,' #Link for MIT stats
    al="https://www.mit.edu/admissions-aid/" #admission link
    ow="https://www.mit.edu/"                #official website
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])

def HavardUniversity ():
    print ('''Harvard College is a close-knit undergraduate community within Harvard University. With world-class faculty, groundbreaking research opportunities, and a commitment to a diverse environment of bright, talented students, Harvard is more than just a place to get an education—it's where students come to be transformed.
            From library and museum collections to arts, athletics, and service, Harvard’s campus resources are unparalleled. Teaching and research are integral to Harvard College—students learn from faculty of the highest caliber, conduct their own investigations, and contribute to research in labs and libraries

            At the heart of Harvard College are the Houses, where students live and learn alongside their peers, faculty members, and graduate students. As a smaller home within the College and University, each House offers an enriching and supportive environment where students grow as individuals and as members of their community.''')

    al="https://college.harvard.edu/admissions"  #<- admission link
    ow="https://www.harvard.edu/"                #<- official website
    stat='https://www.topuniversities.com/universities/harvard-university#wurs'  #<- stats
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])

def UniversityofOxford ():
    print ('''The college system is one of the many distinctive and special features of student life at Oxford. Oxford’s colleges are independent and self-governing, and relate to the University in a federal system like that of the United States. 

The University has 45 colleges. This includes 6 permanent private halls (PPHs), which were founded by various Christian denominations and still retain their religious character. 

Oxford’s colleges are small, multidisciplinary communities. Each one has students, academic staff and administrative staff. Most colleges offer meals, libraries, accommodation, sports, events and other opportunities to enrich your Oxford experience. The colleges have much in common, but each has its own character and history.

All graduate students belong to a department or faculty and a college or hall, except those taking non-matriculated courses. Supervision and teaching will be provided by your academic department, so no matter which college you belong to, this won't limit your access to potential supervisors or teaching staff; your course content is the same. 

The benefits of Oxford colleges
The collegiate system is at the heart of the University’s success. Your college can provide support, facilities and membership of a friendly and stimulating academic community. 

Community
Within your college, you’ll have the opportunity to meet academics and fellow students from around the world, and often from a broad range of subjects. You might find yourself debating your work in college seminars, over meals in the dining hall or in college accommodation late into the evening. Your college will give you the chance to establish a new circle of friends quickly, and get involved with a wide range of events and activities.

As a graduate student you’ll belong to your college’s Middle Common Room (MCR) or Graduate Common Room (GCR), which is a student organisation as well as a physical room in college. Each college MCR usually elects a committee, who aim to foster a sense of community by organising social activities, promoting student well-being and representing student voices.

Facilities
All colleges provide library and IT facilities, welfare support, and sports and social events. Colleges often have accommodation available for rent by their graduate students, although most aren't able to guarantee accommodation. You aren’t obliged to make use of college facilities, but many graduate students find that their college greatly enriches their time at Oxford in a variety of ways.

''')

    stat='https://www.topuniversities.com/universities/university-oxford#wurs' #<- stats
    ow="https://www.ox.ac.uk/" #<- official website
    al="https://www.ox.ac.uk/admissions" #<- admissions website
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def CaliforniaInstituteofTechnology (): #California Institute of Technology (Caltech)
    print (''' The California Institute of Technology (Caltech) is a world-renowned science and engineering research and education institution, located in Pasadena, California, around 11 miles northeast of downtown Los Angeles. 

    Caltech has a high research output as well as many high-quality facilities such as the Jet Propulsion Laboratory (owned by NASA), the Caltech Seismological Laboratory, and the International Observatory Network.  It’s among a small group of institutes of technology in the United States primarily devoted to teaching technical arts and applied sciences, and its fiercely competitive admissions process ensures only a small number of the most gifted students are admitted.

    The university was founded as a preparatory and vocational school by Amos G. Throop in 1891, with the mission “to expand human knowledge and benefit society through research integrated with education”. It became a major hub of US scientific research in the early 20th century and was instrumental to the United States’ war effort during World War II. 

    Today, it is home to the Einstein Papers Project, an initiative seeking to preserve, translate and publish selected papers from the estate of Albert Einstein. It has also established an energy innovation hub that aims to discovery revolutionary methods of generating fuels directly from sunlight. 

    Caltech’s 124-acre campus is within walking distance of Old Town Pasadena and the Pasadena Playhouse District, and the two locations are frequent getaways for students. Life on campus is rich with social activities, clubs, associations and recreational facilities. Intercollegiate sport is taken very seriously, with the Caltech Beavers (the beaver – nature’s engineer – is the college’s mascot) competing in 13 intercollegiate sports. 

    Caltech also offers excellent opportunities for the study and performance of music, theater, and the visual arts, all activities that play a vital role in realizing Caltech’s mission to role in realizing the Institute's mission of "educating outstanding students to become creative members of society". Providing a touch of grandeur, the Athenaeum is a stately building in the center of the campus where members can go for formal and informal dining, meetings, rendezvous and private parties. 

    The balance at Caltech between a rigorous academic curriculum and activities that promote personal development ensures time spent there for students is both formative and an invaluable staging post to a successful career.  Although it may lack the reputation of Ivy League universities or the likes of Oxford and Cambridge, Caltech is undoubtedly one of the best universities in the world, a fact reflected in all the university rankings, which regularly single out technology and engineering as the school’s key academic strengths. ''')
    stat='https://www.topuniversities.com/universities/california-institute-technology-caltech#wurs'# stats
    ow="https://www.caltech.edu/" #offical website           
    al="https://www.caltech.edu/admissions-aid" #admissions link
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])



def ETH (): #ETH Zurich - Swiss Federal Institute of Technology
    print ('''
ETH Zurich is one of the world's leading universities in science and technology and is known for its cutting-edge research and innovation. It was established in 1855 as the Swiss Federal Polytechnic School, and a century and a half later the university can count 21 Nobel laureates, 2 Fields Medalists, 2 Pritzker Prize winners, and 1 Turing Award winner as alumni, including the great Albert Einstein himself. 

The university, referred to in English as the Swiss Federal Institute of Technology Zurich, has 16 departments that offer academic education and conduct scientific research in subjects ranging from engineering and architecture to chemistry and physics. 

Education at ETH Zurich combines solid theory with practical application, and most degree programs build on strong mathematical foundations. For undergraduates the main teaching language is German, while most master's programs and doctoral studies are in English.

Located in Zurich, Switzerland's largest city, ETH Zurich is largely based on a modern main campus built on a hill in the outskirts of the town. Students at ETH have twice as many lectures as those at other Swiss institutions, but can still attend regular exhibitions, plays and concerts, as well as take advantage of the regular symposia and conferences on campus, where some of the best minds in science come to speak. 

ETH students like to exercise their bodies as well as their minds, and there are various sports events held on campus, of which the largest is an annual SOLA relay race in 14 sections, taking place over a total distance of 140 kilometers. More than 900 teams have been known to take part at once in the annual spectacle. 

Since the 1880s, students have also been able to show off their best moves at the Polyball, a classic ball event featuring a live orchestra and famous national singers, in which 10,000 dancers, music-lovers and partygoers descend on ETH’s extensively decorated main building for what is usually an unforgettable night.

''')

    stat='https://www.topuniversities.com/universities/eth-zurich-swiss-federal-institute-technology#wurs'#stats
    ow="https://ethz.ch/en.html" #official website       
    al="https://ethz.ch/en/studies/registration-application/bachelor/other-certificates.html"#admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def UniversityofCambridge (): #University of Cambridge
    print (''' Located in the center of the ancient city of Cambridge, 50 miles north of London, the University of Cambridge is a collegiate public research institution that serves more than 18,000 students from all corners of the globe. 

The university consists of numerous listed buildings and is divided into 31 autonomous colleges, with many of the older ones situated on the famous river Cam. Applications are made directly to the individual colleges, rather than to the university overall. You can live and are often taught within your college, receiving small group teaching sessions known as college supervisions. 

Six academic schools – Arts and Humanities, Biological Sciences, Clinical Medicine, Humanities and Social Sciences, Physical Sciences, and Technology – are spread across the university’s colleges, housing roughly 150 faculties and other institutions. 

Founded in 1209, the University of Cambridge’s 800-year history makes it the fourth-oldest university in the world and the second-oldest university in the English-speaking world. Cambridge students make up 20 percent of the town's population and most of the older colleges are situated near the city center. Its notable buildings give the city of Cambridge a unique character, and include King's College Chapel, the history faculty building designed by James Stirling and the Cripps Building at St John's College.

Cambridge is widely acknowledged as a vibrant place to be a student. On the academic side, the university is home to over 100 libraries, which hold more than 15 million books in total. There are also nine world-renowned arts, scientific and cultural museums such as Kettle’s Yard and the Fitzwilliam Museum, which are open to the public throughout the year, as well as a botanical garden. 

Extracurricular activities give you the chance to get involved with anything from the university’s renowned student drama societies, which spawned the likes of comedy group Monty Python, to music, politics and hundreds of other clubs and societies. The sports scene at Cambridge is huge too, with state-of-the-art facilities and over 80 sports on offer with teams for novices and experts alike. 

With its reputation for academic excellence and traditional scholarly values, the University of Cambridge often ranks among the very top universities in the world for teaching, research, and international outlook. The university has educated eminent mathematicians, scientists, politicians, lawyers, philosophers, writers, actors and heads of''')

    stat='https://www.topuniversities.com/universities/university-cambridge#wurs' #stats
    ow="https://www.cam.ac.uk/" #official webst
    al="https://www.undergraduate.study.cam.ac.uk/applying" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def UCL (): #UCL
    print (''' Where novel thinking is nurtured and encouraged

UCL is a diverse community with the freedom to challenge, to question, and to think differently. Our community pursues academic excellence, breaks boundaries and makes a positive impact on real world problems.

An Academic Powerhouse

UCL is 8th in the world, 4th in Europe, 1st in London in the QS World University Rankings 2020. There has been 29 Nobel laureates among its former staff and students; a winner in every decade since the Prize started.

World Leading Research University

At the very heart of UCL’s mission is our research. We were rated the top university in the UK for research strength in the last Research Excellence Framework (REF 2014). We offer over 675 postgraduate taught, research and initial teacher education programmes across a wide range of disciplines, and encourage our community to work across traditional subject boundaries. UCL's research-based teaching methodology means that research is integrated into many of our degrees and students have the opportunity to make an original contribution to their field of study. Find out about our graduate programmes.  

London’s Global University

UCL sits at the heart of one of the world’s most dynamic cities, meaning you are perfectly placed to take advantage of everything London has to offer. We were the first university in England to welcome women to university education, and the first university in England to welcome students of any religion or social background. UCL has 18,000 students from outside the UK, with over 150 countries represented, providing a truly global perspective.

Disruptive Thinking Since 1826

For nearly two centuries we’ve confronted humanity’s biggest issues, and today we continue our heritage of disruptive thinking. Through our research, many minds at UCL work together to improve lives and communities and create real world impact. Read about some of the disruptive discoveries from UCL at www.ucl.ac.uk/made-at-ucl/

Your Future

At UCL we know that students choose to enter graduate study for a myriad of reasons, and we are deeply committed to supporting our student’s aspirations and enhancing their skills and employability. UCL Careers helps students to find their perfect career, develop their professional skills or start their own business through one-to-one guidance and events, as well as a variety of careers information. Recruitment and networking events help students improve their knowledge of a particular industry sector and specific employers. For students interested in starting a business, UCL Innovation and Enterprise gives expert advice and practical support, as well as networking opportunities.

Be Inspired

If you want to find out more about the impact that our ground-breaking research and discoveries have on people, lives and communities, listen to our #MadeatUCL Disruptive Discoveries podcast. We bring you closer to the researchers answering life’s big questions, from green infrastructure, to artificial intelligence, space exploration, to treating cancer.''')


    stat='https://www.topuniversities.com/universities/ucl#wurs' #stats
    ow="https://www.ucl.ac.uk/" #official wbst
    al="https://www.ucl.ac.uk/" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def ImperialCollegeLondon (): #https://www.ucl.ac.uk/
    print (''' Ranked 9th in the world in the QS World University Rankings® 2020, Imperial College London is a one-of-a-kind institution in the UK, focusing solely on science, engineering, medicine and business. Imperial offers an education that is research-led, exposing you to real world challenges with no easy answers, teaching that opens everything up to question and opportunities to work across multi-cultural, multi-national teams.


Imperial is based in South Kensington in London, in an area known as ‘Albertopolis’, Prince Albert and Sir Henry Cole’s 19th century vision for an area where science and the arts would come together. As a result, Imperial’s neighbors include a number of world leading cultural organizations including the Science, Natural History and Victoria and Albert museums; the Royal Colleges of Art and Music; the English National Ballet; and the Royal Albert Hall, where all of their students also graduate.

There is plenty of green space too, including two Royal Parks (Hyde Park and Kensington Gardens) within 10 minutes’ walk of campus. Travel to and from the area is also really easy as it’s served by three Tube lines and many bus routes.

One of the most distinctive elements of an Imperial education is that students join a community of world-class researchers. The cutting edge and globally influential nature of this research is what Imperial is best known for. It’s the focus on the practical application of their research – particularly in addressing global challenges – and the high level of interdisciplinary collaboration that makes their research so effective. Read more about their research impact here.

The number of award winners, Nobel Prize holders and prestigious Fellowships (Royal Society, Royal Academy of Engineering, Academy of Medical Sciences) amongst their staff is a testament to the outstanding contributions they have made in their respective fields.

Imperial is one of the most international universities in the world, with 59% of its student body in 2018-19 being non-UK citizens and more than 140 countries are currently represented on campus. Meanwhile, the College’s staff, like their students, are diverse in their cultural backgrounds, nationalities and experiences.''')

    stat='https://www.topuniversities.com/universities/imperial-college-london#wurs' #stats
    ow="https://www.imperial.ac.uk/"#official wbst
    al="https://www.imperial.ac.uk/study/ug/apply/" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])

def UniversityofChicago (): #University of Chicago
    print (''' Established in 1856, the University of Chicago is a private research university based in the urban center of Chicago, the third most populous city in the United States. Outside of the Ivy League, Chicago is one of America’s top universities, and holds top-ten positions in various national and international rankings. 

Beyond the arts and sciences, Chicago has a glowing reputation for its professional schools, including the Pritzker School of Medicine, the Booth School of Business, and the Harris School of Public Policy Studies. University of Chicago alumni are responsible for the development of many academic disciplines, such as sociology, economics, law, and literary criticism.  

The college’s crest sees a phoenix rising from the ashes, a reference to the fire, foreclosure, and demolition of the Old University of Chicago campus, with the current University of Chicago emerging triumphantly in its place in 1890. The old university was founded through a land endowment from the controversial senator Stephen Douglas, a supporter of slavery who authored the Kansas-Nebraska act. By contrast, the new University of Chicago was co-educational and funded through donations from wealthy Chicagoans and the oil magnet John D. Rockefeller. 

Today, the University of Chicago has approximately 16,000 students enrolled, with a male to female ratio of 56:44. A quarter of all students hail from overseas, a nod to the institution’s progressive credentials. 

Students run more than 400 clubs and societies, which consist of a typical mix of sports teams, arts, cultural and religious groups, academic and political groupings, and societies that promote eclectic common interests. Among the more famous examples are the University of Chicago bowl team, which has won 118 tournaments and 15 national championships, while the university's competitive Model United Nations team was the top ranked team in North America in 2013–14 and 2014–2015. 

If you have an interest in media and film, then you’re well catered for: the university is home to the longest continuously running student film society Doc Films and publishes several newspapers and magazines. Budding thespians can join renowned improvisational theater troupe Off-Off Campus, or learn how to broadcast at the university-owned radio station WHPK.

Notable faculty members past and present include 29 Nobel laureates and former US president Barack Obama. Illustrious alumni come in practically every field, including the novelists Philip Roth and Saul Bellow, political movers and shakers such as pollster Nate Silver and Obama strategist David Axelrod, pioneering balloonist Jeannette Piccard, and the fictional archaeologist Indiana Jones. 

''')
    stat='https://www.topuniversities.com/universities/university-chicago#wurs' #stats
    ow="https://news.uchicago.edu/story/echo-game-brings-students-together-and-keeps-them-safe" #official website
    al="https://www.uchicago.edu/admissions/" #admission
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])
    


def NanyangTechnologicalUniversity(): #ntu
    print (''' Young and research-intensive, Nanyang Technological University, Singapore (NTU Singapore) is placed 11th globally, and 1st among the world’s best young universities for five consecutive years (QS university rankings).
 
Home to 33,000 students, NTU offers engineering, science, business, humanities, arts, social sciences, and education, and has a joint medical school with Imperial College London.
 
Ranked the top university in the world for citations in artificial intelligence (Nikkei and Elsevier 2017) for the period 2012-2016, NTU is embracing digital technologies for better learning and living as part of its Smart Campus vision. It has partnerships with the world’s leading technology companies such as Alibaba, Rolls-Royce, BMW, Volvo, Delta Electronics, and Singtel in many areas of societal importance and impact that include artificial intelligence, data science, robotics, smart transportation, computing, personalised medicine, healthcare and clean energy.
 
The NTU Smart Campus is not only a living testbed of tomorrow’s technologies, but it is also frequently listed among the world’s Top 15 most beautiful university campuses. It has 57 Green Mark-certified (equivalent to LEED-certified) building projects comprising more than 230 buildings, of which 95% are certified Green Mark Platinum.
 
Apart from its main campus, NTU also has a medical campus in Novena, Singapore’s healthcare district.''')
    ow="https://www.ntu.edu.sg/Pages/home.aspx" #official wbst
    al="https://admissions.ntu.edu.sg/Pages/Home.aspx"#admission
    stat='https://www.topuniversities.com/universities/nanyang-technological-university-singapore-ntu#wurs'#stats
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def NationalUniversityofSingapore (): #NUS
    print (''' A leading global university centred in Asia, the National University of Singapore (NUS) is Singapore’s flagship university, which offers a global approach to education and research, with a focus on Asian perspectives and expertise.

NUS has 17 faculties and schools across three campuses. Its transformative education includes a broad-based curriculum underscored by multi-disciplinary courses and cross-faculty enrichment. Over 38,000 students from 100 countries enrich the community with their diverse social and cultural perspectives. NUS also strives to create a supportive and innovative environment to promote creative enterprise within its community.

The 17 Schools in NUS include:  

Arts and Social Sciences
Business
Computing
Continuing and Lifelong Education
Dentistry
Design and Environment
Duke-NUS Medical School
Engineering
Integrative Sciences and Engineering
Law
Medicine
Music
Public Health
Public Policy
Science
University Scholars Programme
Yale-NUS College

NUS takes an integrated and multi-disciplinary approach to research, working with partners from industry, government and academia, to address crucial and complex issues relevant to Asia and the world. Researchers in NUS’ Schools and Faculties, 30 university-level research institutes and centres, and Research Centres of Excellence cover a wide range of themes including: energy, environmental and urban sustainability; treatment and prevention of diseases common among Asians; active ageing; advanced materials; risk management and resilience of financial systems. The University’s latest research focus is to use data sciences, optimisation research and cyber security to support Singapore's Smart Nation initiative.''')
    ow="http://www.nus.edu.sg/" #official wbst
    al="http://www.nus.edu.sg/admissions" #admissions
    stat='https://www.topuniversities.com/universities/national-university-singapore-nus#wurs' #stats
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])




    

def PrincetonUniversity(): #Princeton University
    print (''' Princeton is one of the oldest and most prestigious universities in the United States. It was founded in 1746 and moved to its current site in New Jersey in 1896. 

Princeton is renowned for the spectacular greenery of its campus and for the architectural splendor of some of its landmark buildings, such as its Lewis Library, which was designed by Frank Gehry. Its student body is relatively small, with fewer than 10,000 enrolled in total, and international students make up 12 per cent of undergraduates. 

Princeton is one of the world’s foremost research universities, and has educated two US presidents, James Madison and Woodrow Wilson. Other distinguished graduates include Michelle Obama, actors Jimmy Stewart and David Duchovny, Google chairman Eric Schmidt and Apollo astronaut Pete Conrad.

Princeton was founded by New Light Presbyterians to provide training to its ministers. After the American Civil War, the college expanded, and its curriculum was overhauled. Around the turn of the 20th century, it officially became a university and its famous graduate school opened. 

Today’s Princeton provides undergraduate and graduate education in the humanities, social sciences, natural sciences, and engineering as well as offering a number of professional degrees. 

Princeton’s main campus is spread across 500 acres and has around 180 buildings, including 10 libraries. The main campus was named one of the most beautiful in the United States by New York’s Travel+Leisure magazine. Most Princeton students live, eat, study, work, and are at leisure on campus.  

The Ivy League institution guarantees accommodation to all of its undergraduate students across the four years of their degree and is committed to building a diverse campus community. Residential colleges offer a variety of academic, social, cultural and recreational programs, and opportunities abound for students to engage in interests beyond their academic study, whether that be writing for a literary publication, learning the science of beekeeping, or singing with an a capella group. 

The university is within easy reach of both New York City and Philadelphia, with the “Dinky” shuttle train providing a regular one-hour service to both cities. 

Studying at Princeton surrounded by natural beauty and architectural gems brings the best out in students. Several alumni and faculty members have been awarded Nobel prizes, and the university is consistently ranked in the top ten worldwide. Admissions are need-blind and, through a combination of grants and college jobs, few students graduate in debt – even though 60 percent of incoming students receive financial aid. ''')

    stat='https://www.topuniversities.com/universities/princeton-university#wurs'#stats
    ow="https://www.princeton.edu/" #official website
    al="https://www.princeton.edu/admission-aid" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])

def CornellUniversity() : #cornell university
    print (''' Since its founding, Cornell has been a co-educational, non-sectarian institution where admission has not been restricted by religion or race. These are liberal traditions that Cornell holds dear: a recent article in the Cornell Chronicle heralded the first all-female class admitted to its famous Farrier program in veterinary science. Cornell was also the first university to offer degrees in journalism and the first to teach modern Far Eastern languages. 

The main campus of Cornell is on East Hill in Ithaca, New York, overlooking the city and Cayuga Lake. It spreads over 2,300 acres and comprises laboratories, administrative buildings, and almost all the campus' academic buildings, athletic facilities, auditoriums, and museums. 

The architecture is an eclectic mix of Collegiate Gothic, Victorian, and Neoclassical buildings, international and modernist structures. There are other campuses and facilities in New York City itself such as the medical campus Weill Cornell in Manhattan, and the engineering campus Cornell Tech. Outside New York, Cornell has an outpost in the gulf state of Qatar, which is the first American medical college to open outside of the United States. 

Ithaca campus sits at the heart of the Finger Lakes region, surrounded by green space and natural beauty. Students here are as likely to be found sitting under a tree with their nose in a book as they are taking advantage of the many clubs, societies and activities Cornell has to offer. 

First-year undergraduates live on North Campus, while upper-level students often hone in on the communities that they have found, opting for a fraternity or sorority, a co-op, a themed residence hall, or an apartment off campus. 

There are more than 1,000 organizations on campus, ranging from skateboarding to volunteer programs. Sporty or outdoorsy students can take part in courses as diverse as caving and rope climbing, and there are four sports centers for the fitness inclined. 

Food lovers are also well catered for, with Cornell voted in the top ten universities for food, with more than 30 dining facilities across campus. ''')

    stat='https://www.topuniversities.com/universities/cornell-university#wurs'#stats
    ow="https://www.cornell.edu/" #official wbst
    al="https://www.cornell.edu/admissions/" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def UniversityofPennsylvania (): #University of Pennsylvania
    print (''' The University of Pennsylvania is a private Ivy League research university located in the city of Philadelphia. It was founded in 1740 by Benjamin Franklin, one of the United States’ founding fathers, who was eager to create a school to educate future generations. 

Franklin advocated a concept of higher education that focused not merely on the education of the clergy, but on teaching knowledge of arts and humanities, as well as the practical skills needed to make a living and to do public good. His maxim of “well done is better than well said” lives on today through its commitment to inclusive policies and innovation. 

As of fall 2017, there were 21,599 students studying at Penn, split equally between undergraduate and graduate students. Penn has a strong focus on interdisciplinary learning and research, offering double degree programs, unique majors and academic flexibility. This means competition to study at Penn is fierce, particularly at undergraduate level. The admission rate for the class of 2021 was 9.3 percent, of which 46 percent were either black, Hispanic Asian, or Native American. Unusually for an Ivy League school, women comprise over half (54 percent) of all students enrolled.  

Penn’s core campus covers more than 279 acres in a contiguous area of West Philadelphia's University City. All of Penn's schools and most of its research institutes are located on this campus, with the surrounding neighborhood including restaurants and pubs, a large supermarket and cinema. 

Student life at Penn serves up opportunities to discover new interests and passions galore, through a wide diversity of social, political, religious, and cultural activities. There are cultural centers and one-of-a-kind museums on campus that allow the arts to play a leading role in student life such as the Annenberg Center for the Performing Arts, the Arthur Ross Gallery, and Institute of Contemporary Art, which are all major cultural destinations and easy for Penn students to access. 

The university also takes sports and recreation very seriously, with students taking part in ice hockey, athletics and joining a variety of competitive, instructional and recreational sports clubs.  

With its arts and sciences programs ranking in the top 10 nationally, and the employment prospects for its students among the brightest (Penn boasts one of the highest numbers of graduates who go on to become Fortune 500 CEOs), there is little doubt that the University of Pennsylvania deserves its Ivy League status and reputation.  ''')

    stat='https://www.topuniversities.com/universities/university-pennsylvania#wurs' #stats
    ow="https://www.upenn.edu/"  #oficial wbst
    al="https://www.upenn.edu/admissions" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])

def TsinghuaUniversity (): #Tsinghua University
    print (''' Students looking for great engineering and computer science programs need look no further than Tsinghua University in Beijing, which since 2015 has been ranked as one of the best in the world for both disciplines. 

Tsinghua University was established in 1911 in the wake of the anti-colonialist Boxer Rebellion, which saw the US fine China $30m as punishment. In 1909, President Theodore Roosevelt negotiated with Congress a reduction in the sum, with the leftover money earmarked for university scholarships for Chinese students to study in the US. Tsinghua University was established as a preparatory school for the students’ trips abroad. 

Today, Tsinghua’s motto of “self-discipline and excellence” has taken it far. Most university rankings place Tsinghua among the best universities in China, and famous alumni include President Xi Jinping himself, who graduated with a degree in chemical engineering in 1979. Tony Blair, Henry Kissinger, and Bill Clinton are among the distinguished guests who have spoken at Tsinghua. 

The university is academically organized into 20 schools and 57 departments covering a broad range of subjects, including science, engineering, arts and literature, social sciences, medicine. Xinya College was established in 2014 as the school’s residential liberal arts college as part of a series of reforms to undergraduate education. Unlike other Tsinghua students who must choose a specific major upon enrollment, Xinya students can declare their majors at the end of their freshman year.

The campus of Tsinghua University is located in northwest Beijing, in the Haidian district, on the former site of the Qing Dynasty royal gardens. As such it retains Chinese-style landscaping as well as traditional buildings, although many of its buildings are also western in style, reflecting its American heritage. Like its archrival Peking, Tsinghua is known for having one of the most beautiful university campuses. 

On campus, students keep themselves occupied with more than just academic study (although the heavy workloads mean studying is always a priority). There are more than 110 student clubs and associations covering interests such as science and technology, health and fitness, humanities, arts and public welfare. 

Overseas students are particularly encouraged to join in the fun, with a host of extracurricular such as welcome parties, New Year’s parties, graduation parties, and visits to cultural and historical landmarks. ''')


    stat='https://www.topuniversities.com/universities/tsinghua-university#wurs' #stats
    ow="https://www.tsinghua.edu.cn/en/index.htm"  #official wbst
    al="https://www.tsinghua.edu.cn/en/Admissions.htm"  #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def YaleUniversity() : #Yale University
    print (''' Yale University is a private research university and a member of the prestigious Ivy League, a group of America’s most celebrated higher education institutions. Situated in New Haven, Connecticut, the first planned city in America, Yale was founded by English Puritans in 1701, making it the third-oldest higher education institution in the United States. 

Today, the city, which is part of the New York metropolitan area, is very much dominated by Yale, though it’s also billed as the “Cultural Capital of Connecticut”. According to the New York Times, New Haven is also extremely picturesque, with “art almost everywhere you look”.

Yale University’s central campus spans 260 acres and includes buildings from the mid-18th century. The university is organized into 14 schools: the original undergraduate college, the Yale Graduate School of Arts and Sciences and 12 professional schools. 

Undergraduates follow a liberal arts curriculum which allows you to think and learn across disciplines before deciding upon a major. Perhaps its most distinctive feature, Yale undergraduates are organized into a social system of residential colleges, which allows them to experience the cohesiveness and intimacy of a small school while still enjoying the cultural and scholarly resources of a large university.

A recently unveiled portrait of Barack Obama was by a Yale alumnus, and strolling across the Yale campus, you’ll find that you’re surrounded by public art. Be it in courtyards or plazas, lobbies or lecture halls, art at Yale inspires reflection and offers aesthetic pleasure. 

College life is similarly rich, reflecting the diversity of cultures and nationalities on campus. There’s always a packed arts calendar which includes exhibitions at world-class museums and galleries. There’s also a Tony Award-winning theater, Yale Cabaret – a theater-restaurant run by students – and hundreds of student groups, ranging from the serious to the silly. 

On top of this, you’ll also find the usual array of top quality sports facilities, a golf course and centers for tennis, polo, sailing, ice hockey, and more as well as competitive sports, with over 30 men’s and women’s varsity teams. 

To study at Yale is to join great company: four Yale graduates signed the American Declaration of Independence, and the university has educated five US presidents: William Howard Taft, Gerald Ford, George H. W. Bush, Bill Clinton and George W. Bush. It is rightly regarded as one of America and the world’s most prestigious universities, with competition to be admitted as fierce as it gets. ''')

    stat='https://www.topuniversities.com/universities/yale-university#wurs' #stats
    ow="https://www.yale.edu/" #official wbst
    al="https://www.yale.edu/admissions" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def ColumbiaUniversity (): #Columbia University
    print (''' Established in 1754, Columbia University is a private Ivy League research university in Upper Manhattan, New York City. It was established as King's College by royal charter of George II of Great Britain and renamed Columbia College in 1784 following the American Revolutionary War. 

With an undergraduate acceptance rate of 5.8 percent, Columbia is currently the third most selective college in the United States and the second most selective in the Ivy League after Harvard. Its first president was none other than the literary great Samuel Johnson, and over the years Columbia has produced numerous distinguished alumni, from Oscar winners and Nobel laureates to Supreme Court judges. Three US Presidents and the authors of the Declaration of Independence and American Constitution were also schooled at Columbia. It also runs the highly distinguished Pulitzer Prize, an annual award for achievements in journalism, literature and musical composition. 

The university is organized into 20 schools, including undergraduate schools such as Columbia College, the Fu Foundation School of Engineering and Applied Science, and the School of General Studies, as well as graduate schools such as Columbia Law School, Columbia College of Physicians and Surgeons, Columbia Journalism School and Columbia Business School. It also had global research outposts across the world. Its total student body numbers around 28,000 and is comprised mainly of postgraduates, with roughly 8,500 undergraduate students. 

Columbia’s main campus is Morningside Heights, occupying around six city blocks in the Morningside Heights district of New York. It’s home to the neo-classical Butler library, one of the largest buildings on campus, and almost two dozen undergraduate dormitories. The university also owns 7,800 apartments in the local area, which house faculty members, students, and staff. 

The campus was designed along Beaux-Arts principles and was a late 19th century vision of a campus where all disciplines could be taught. Some of its standout features include the Low Memorial Library, a National Historic Landmark, the site of the invention of FM radio, and the location where the nuclear fission of uranium first took place. 

More significant for students are The Steps, a long series of granite steps which are a popular hangout and meeting place, and the bronze figure of Alma Mater, a female figure draped in an academic gown who serves as a daily reminder to students of their scholarly duties. ''')

    stat='https://www.topuniversities.com/universities/columbia-university#wurs' #stats
    ow="https://www.columbia.edu/" #official wbst
    al="https://www.columbia.edu/content/admissions" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def EPFL (): #EPFL
    print (''' The École polytechnique fédérale de Lausanne (EPFL) is a research institute and university in Lausanne, Switzerland, specializing in the natural sciences and engineering. 

Its roots can be traced back to the foundation of a private school in 1853, which to start with only had 11 students. Those days are long gone though, with the modern day EPFL one of two Swiss Federal Institutes of Technology and student numbers in Lausanne now totaling over 10,000. 

Located in the French-speaking part of Switzerland, EPFL is twinned with the Swiss Federal Institute of Technology in Zurich (ETH Zurich). As part of its research and teaching activities, EPFL is one of the only universities to run a nuclear reactor, a fusion reactor, a Gene/Q Supercomputer, and have P3 bio-hazard facilities.

EPFL has a very singular admissions process, which, for would-be undergraduates who are Swiss nationals, is not selective at all. At the end of freshman year, however, a block exam determines whether students can continue or have to repeat the year, with many home students dropping out entirely at this point. 

The EPFL campus lies on the shores of Lake Geneva and consists of 65 buildings across 136 acres. Facilities include banks, bars, two museums – the Musee Bolo and Archizoom – as well as bars, restaurants and cafeterias. 

There are students of 112 different nationalities here, though as of 2014 women made up only 27 percent of the student body. Life on campus is vibrant, with many student-formed clubs and associations providing social and recreational opportunities. 

A wide range of sports and leisure facilities keep students physically active while studying. EPFL also has an active student media, publishing the monthly newspaper Flash and there are daily broadcasts on the student radio station. 

Another priority on campus is the arts, with the university holding several annual music festivals each year. The largest is Balélec Festival, where 15,000 visitors descend upon the university to watch 30 concerts on two outdoor and four indoor stages.

''')

    stat='https://www.topuniversities.com/universities/epfl#wurs' #stats
    ow="https://www.epfl.ch/en/" #official site
    al="https://www.epfl.ch/education/admission/"#admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def TheUniversityofEdinburgh (): #The University of Edinburgh
    print( ''' Inspiring the world since 1583

The University of Edinburgh is one of the world's top universities, consistently ranked in the world top 50*, and placed 20th in the 2020 QS World University Rankings. Our entrepreneurial and cross-disciplinary culture attracts students and staff from across the globe, creating a unique Edinburgh experience. We provide a stimulating working, learning and teaching environment with access to excellent facilities. We attract the world's best, from Nobel Prize winning laureates to future explorers, pioneers and inventors.

Study with us

As host to more than 40,000 students from some 156 countries, the University of Edinburgh continues to attract the world’s greatest minds.

We offer a range of ways to study, from on-campus taught programmes to online part-time study. We are the largest provider of online distance learning in the Russell Group of UK research-intensive universities, and offer more than 70 online programmes. Our flexible and supportive online learning programmes are an increasingly popular choice for students looking to balance further study with professional or family commitments.

Teaching and research excellence

The latest report from the Quality Assurance Agency awarded us the highest rating possible for the quality of the student learning experience. At postgraduate level, we offer more than 300 taught masters courses and 180 research areas across our three Colleges:

- College of Arts, Humanities and Social Science 
- College of Medicine and Veterinary Medicine
- College of Science and Engineering

Our position as one of Britain’s leading research universities was reaffirmed by the results of the 2014 Research Excellence Framework (REF). The REF rates 83% of our research activity as world-leading or internationally excellent, ranking us fourth in the UK based on the quality and breadth of our research.

We are associated with 19 Nobel Prize winners, who are alumni of the University of have been members of academic staff here and have long enjoyed a spirit of innovation and collaboration and continue to do so today. We are proudly open to everyone, bringing people with new outlooks and perspectives together in an international community that is establishing the data capital of Europe, tackling climate change and paving the way for new fertility treatments. Our scientists are seeking cures for cancer, repurposing drugs to improve treatments for the Covid-19 Coronavirus and contributing to the global search for a vaccine.

Joining the University as a student provides you with a unique opportunity to work with some of the most influential academics in your chosen field. At Edinburgh, you will develop specialist skills, deepen your understanding and gain new insights and perspectives to equip you for your career ahead.

Global connections

Our ambitious internationalisation strategy aims to provide world-class experiences for students and ensures the teaching and research we deliver offers global benefits.

Collaborations and international partnerships

We collaborate with a host of world-leading institutions in fields as diverse as e-science, engineering, life and medical sciences and arts and culture. We’re also a member of the global research network Universitas 21, and the European networks COIMBRA group, as well as UNICA, LERU, and UNA Europa

Our students are crucial to our continued success and development and, along with our staff, they forge research links through regular travel and overseas exchanges. We take pride in our partnerships with other institutions such as the California Institute of Technology, University of Copenhagen, University College Dublin, the University of Melbourne, Peking University, the University of Delhi and Zhejiang University– to name but a few.

Alumni

As a graduate of Edinburgh, you will join a lifelong community of more than 200,000 like-minded people from across the world. This professional and social network provides a lifetime of support with clubs and contacts across the world and a range of groups and resources online. For a taste of what our alumni are doing today, see our monthly update where they share their experiences, showcase their career paths, and impart their wisdom.

Visit our alumni pages for more details.

Our famous alumni include historical greats such as Joseph Black, who discovered carbon dioxide, and philosopher David Hume, whose ideas laid the foundations of contemporary thought. Edinburgh alumni also include 21st century luminaries, such as Harry Potter creator JK Rowling and Olympians Dame Katherine Grainger and Sir Chris Hoy.

 

Fees

Tuition fees vary by programme and length taken to complete. Visit our tuition fees pages for more information.

Funding and scholarships

Postgraduate study can be a significant financial commitment; however, the range of funding sources available may surprise you. We offer several postgraduate scholarships and studentships to outstanding candidates. Check our scholarship pages for details.''')

    stat='https://www.topuniversities.com/universities/university-edinburgh#wurs' #stats and more info
    ow="https://www.ed.ac.uk/" #official wbst
    al="https://www.ed.ac.uk/studying/admissions" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def UniversityofMichiganAnnArbor(): #University of Michigan-Ann Arbor
    print (''' One of the foremost research universities in the United States, the University of Michigan was founded in 1817, before Michigan had even become a state, and moved from Detroit to what is now its Central campus in Ann Arbor in 1837. 

Michigan spans 780 acres, which is made up of its Central and North campuses, two regional campuses, and a center in Detroit. It has a large student body of around 46,000, with undergraduates numbering two-thirds of that number. 

Michigan has been lauded for having high standards of research, and the university’s comprehensive graduate program offers doctoral degrees in the humanities, social sciences, and STEM fields (science, technology, engineering and mathematics) as well as professional degrees in architecture, business, medicine, law, pharmacy, nursing, social work, public health, and dentistry.

Michigan's body of living alumni comprises more than a half million people, which is one of the largest alumni bases of any university in the world and a valuable resource for current students when it comes to networking and building industry connections.

Around a quarter of all students are accommodated on campus, with many residence halls serving undergraduates, and family housing which is intended mainly for graduates. There are also off-campus apartments, houses, and co-operatives, which generally house upper division and graduate students, as well as ‘theme communities’ within residence halls, where students can immerse themselves among peers with similar interests. 

Michigan has more than 1,000 clubs and societies, including engineering project teams, community service organizations, and charitable projects. The Michigan Marching Band is over 100 years old and has 350 student members, and other noted musical ensembles include the University of Michigan Men’s Glee Club, a men’s chorus with over 100 members. 

Michigan has a history of student activism, and there are a number of groups dedicated to various worth causes. Some, such as the United Students Against Sweatshops (USAS), devote themselves to more left-wing causes, in this case holding to account multinational companies that exploit their workers in factories, but there are also conservative groups such as Young Americans for Freedom, as well as non-partisan groups. 

Cultural and ethnical student organizations help students forge smaller communities from the large university population, and publications such as the Michigan Daily, published five days a week during the Fall and Winter terms, allow students to keep''')

    
    stat='https://www.topuniversities.com/universities/university-michigan-ann-arbor#wurs' #stats
    ow="https://umich.edu/" #offial site
    al="https://admissions.umich.edu/apply" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])





# INIDAN COLLEGES   # INIDAN COLLEGES   # INIDAN COLLEGES   # INIDAN COLLEGES   # INIDAN COLLEGES 
    


def IITBombay (): #IIT Bombay
    print (''' Established in 1958, the second of its kind, IIT Bombay was the first to be set up with foreign assistance. The funds from UNESCO came as Roubles from the then Soviet Union. In 1961 Parliament decreed the  IITs as  ‘Institutes of National Importance'. Since then, IITB has grown from strength to strength to emerge as one of the top technical universities in the world.

The institute is recognised worldwide as a leader in the field of engineering education and research. Reputed for the outstanding calibre of students graduating from its undergraduate and postgraduate programmes, the institute attracts the best students from the country for its bachelor's, master's and doctoral programmes. Research and academic programmes at IIT Bombay are driven by an outstanding faculty, many of whom are reputed for their research contributions internationally.

IIT Bombay also builds links with peer universities and institutes, both at the national and the international levels, to enhance research and enrich its educational programmes. The alumni have distinguished themselves through their achievements in and contributions to industry, academics, research, business, government and social domains. The institute continues to work closely with the alumni to enhance its activities through interactions in academic and research programmes as well as to mobilise financial support.

Over the years, the institute has created a niche for its innovative short-term courses through continuing education and distance education programmes. Members of the faculty of the institute have won many prestigious awards and recognitions, including the Shanti Swaroop Bhatnagar and Padma awards.

Located in Powai, one of the northern suburbs of Mumbai, the residents of the institute reap the advantage of being in the busy financial capital of India, while at the same time enjoying the serenity of a campus known for its natural beauty. A fully residential institute, all its students are accommodated in its 15 hostels with in-house dining; the campus also provides excellent amenities for sports and other recreational facilities.''')

    ow="https://www.iitb.ac.in/en/about-iit-bombay"  #official website
    al="https://www.iitb.ac.in/newacadhome/toadmission.jsp"  #admissions link
    stat="https://collegedunia.com/university/25703-iit-bombay-indian-institute-of-technology-mumbai" #stats
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])



def IITDelhi (): #IIT Delhi
    print (''' Indian Institute of Technology Delhi is one of the 23 IITs created to be Centres of Excellence for training, research and development in science, engineering and technology in India.

Established as College of Engineering in 1961, the Institute was later declared as an Institution of National Importance under the “Institutes of Technology (Amendment) Act, 1963” and was renamed as “Indian Institute of Technology Delhi”. It was then accorded the status of a Deemed University with powers to decide its own academic policy, to conduct its own examinations, and to award its own degrees.

Since its inception, over 48000 have graduated from IIT Delhi in various disciplines including Engineering, Physical Sciences, Management and Humanities & Social Sciences. Of these, nearly 5070 received Ph.D. degrees. The number of students who graduated with B.Tech. degree is over 15738. The rest obtained Master’s Degree in Engineering, Sciences and Business Administration. These alumni today work as scientists, technologists, business managers and entrepreneurs. There are several alumni who have moved away from their original disciplines and have taken to administrative services, active politics or are with NGOs. In doing so, they have contributed significantly to building of this nation, and to industrialization around the world.''')

    ow="https://home.iitd.ac.in/about.php"#official site
    al="http://www.jeeadv.ac.in/"        #admissions link
    stat="https://collegedunia.com/university/25455-indian-institute-of-technology-iit-new-delhi" #stats
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def IITMadras (): #IIT Madras
    print(''' The Indian Institute of Technology Madras is known both nationally and internationally for excellence in technical education, basic and applied research, innovation, entrepreneurship and industrial consultancy. A faculty of international repute, a highly motivated and brilliant student community, excellent technical and supporting staff and an effective administration have all contributed to the pre-eminent status of IIT Madras. The Institute is proud to bear the laureate of being No.1 engineering university in India. More recently, IIT Madras has been given the title of Institute of Eminence.

In 1956, the German Government offered technical assistance for establishing an institute of higher education in engineering in India. The first Indo-German agreement in Bonn, West Germany for the establishment of the Indian Institute of Technology at Madras was signed in 1959.

The Institute was formally inaugurated in 1959 by Prof. Humayun Kabir, Union Minister for Scientific Research and Cultural Affairs. The IIT system has sixteen Institutes of Technology – the first of these to be instituted were at Kharagpur (estb. 1951), Mumbai (estb. 1958), Chennai (estb. 1959), Kanpur (estb. 1959), Delhi (estb. 1961), Guwahati (estb. 1994) and Roorkee (estb. 1847, joined IITs in 2001).
A globally recognised Institute
IIT Madras is a residential institute with nearly 550 faculty, 8000 students and 1250 administrative & supporting staff and is a self-contained campus located in a beautiful wooded land of about 250 hectares. The campus is located in the city of Chennai, previously known as Madras. Chennai is the state capital of Tamilnadu, a southern state in India.

The Institute has sixteen academic departments and a few advanced research centres in various disciplines of engineering and pure sciences, with nearly 100 laboratories organised in a unique pattern.

IIT Madras has been the top-ranked engineering institute in India for four consecutive years as well as  the ‘Best Educational Institution’ in Overall Category in the NIRF Rankings of 2019 put out by the Ministry of Human Resource Development.

Insti Lingo
Any visitor to IIT Madras who spends a few minutes in the campus will find themselves in the midst of conversations that are happening in a different tongue. This is our very own Insti lingo – the IIT Madras lingo – which include words that extend beyond the realm of the bulkiest Oxford Dictionaries or the most exhaustive Websters.

Over the years, our students have developed their own indigenous vocabulary that symbolises the two traits of an IITian that distinguish him from the average guy next door—creativity and brevity. Simple phrases , such as “I crashed da...”, “Psued da.. ” or “Don’t put psued macha!”, will eventually come to make sense to a resident, who will marvel at the ingenuity of the lingo as they come to terms with it. ''')


    ow="https://www.iitm.ac.in/" #official website
    stat="https://www.shiksha.com/college/iit-madras-indian-institute-of-technology-adyar-chennai-3031"  #stats
    al="https://onlinedegree.iitm.ac.in/admissions.html"  #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def IITKanpur (): #IIT Kanpur
    print(''' Indian Institute of Technology (IIT) Kanpur is ranked 5th nationally in Engineering category by NIRF Ranking 2019 and is one of the leading Engineering colleges in India. Currently, there are 5,261 students enrolled in undergraduate and postgraduate programs, including 555 female students. IIT Kanpur features a strong faculty of over 430 Ph.D holding members and a student to teacher ratio of 15.96. 

The institute offers several specializations into undergraduate, postgraduate, integrated and research programs in the field of Engineering, Science, Management, and Design. IIT Kanpur Admissions to B.Tech, B.S, M.Sc, M.Tech./ MS and M.Des are offered through JEE Advanced, JAM. GATE and CEED scores respectively. The college has a dedicated Students’ Placement Office that conducts regular placements every academic year. In 2019, the median annual package reached INR 15 LPA with 437 students getting placed in national and international reputed companies.''')

    stat="https://collegedunia.com/university/25948-indian-institute-of-technology-iit-kanpur"#stats
    ow="https://www.iitk.ac.in/"  #official website
    al="https://iitk.ac.in/new/admissions"  #admission
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def IITKharagpur (): #IIT Kharagpur
    print(''' Indian Institute of Technology (IIT) Kharagpur was the first-ever IIT to be established and is recognized as an institute of national importance. It has been ranked 4th in the Engineering category by NIRF Ranking 2019, making it one of the leading engineering colleges across India. The college has a sizeable faculty of over 780 members including a majority of highly qualified and experienced Ph.D holders and currently has a strength of 8,979‬ students, as of 2019. IIT Kharagpur offers undergraduate, postgraduate, dual degree and doctoral programs in several specializations.  The institute offers B.Tech, B.Arch., Integrated, LLB, LLM, M.Tech., MCP, M.Sc., MBA, EMBA, MMST, and Ph.D. program to the aspirants. Admissions are based on the marks secured by the students in the respective national level entrance examinations including JEE Mains, JEE Advanced, GATE, JAM, CAT etc. Last year, the opening and closing cutoff for admission to B.Tech in Computer Science and Engineering at IIT Kharagpur was 204-283 and 520-980 for male and female candidates respectively. The college offers several facilities including sports, extracurriculars, accommodation, central library etc. IIT Kharagpur also has a great placement record with the first day of the recent placement season of 2019-2020 bringing in over 460 offers from about 30 companies, including many pre-placement offers.
Indian Institute of Technology Kharagpur has been ranked by various recognized platforms among colleges at the national and international level

Ranked 4th in Engineering category by NIRF Ranking 2019.
Ranked 1st in Architecture category by NIRF Ranking 2019.
Ranked 4th in Engineering category by Outlook Ranking 2019
Ranked 5th overall by QS Ranking 2019
Ranked 4th in Engineering category by SuccessCDs Ranking 2019.
Ranked 4th in Engineering category by Jagranjosh Ranking 2019.
Ranked #201 - #250 internationally by TIMES Higher Education Ranking 2020

IIT Kharagpur Scholarship
Merit-cum-means scholarship of INR.1000 p.m. & a tuition fee waiver is awarded to 25% of students admitted under B.Tech, B.Arch, Integrated M.Sc., and 2-year M.Sc program
Assistantship of INR 10000 per month to MMST students
Students admitted to Dual Degree program are provided scholarships at par with B.Tech. students up to 4th year and at par with M.Tech in their 5th year.
Check: IIT Kharagpur Scholarship

IIT Kharagpur Placement
IIT Kharagpur offers training and placement opportunities to candidates through their Career Development Center and Central Placement Cell, working bodies that counsel and provide training to the job aspirants before appearing for an interview. The academic year 2018-2019 saw a successful placement season with a total of 437 students from 4-year undergraduate courses getting placed with reputed companies and MNCs, bringing in a median salary of INR 14.20 LPA. 36 students from 5-year undergraduate courses got placed with a median salary of INR 11.45 LPA, and 29 students from 3-year undergraduate courses with a median salary of INR 8.25 LPA. The past recruiters at the Indian Institute of Technology Kharagpur have been some of the most reputed tech giants such as Amazon, Adobe, Cognizant, Cisco, Cypress, Deshaw and Co, and many more.  Read More: IIT Kharagpur Placement

IIT Kharagpur Faculty
Indian Institute of Technology Kharagpur has a large and diverse faculty of 781 highly qualified and accomplished members. Out of this, 772 of the members hold Ph.Ds in their respective disciplines. The entire faculty of IIT Kharagpur is very experienced and well versed in their subject matter. Members of the faculty are cooperative towards students and always encourage them to ask questions and clarify their concepts as much as they can, by being available to students even outside lectures and classes. The faculty consists of a dedicated team of professors, associate professors and assistant professors.  Click here: IIT Kharagpur Faculty

IIT Kharagpur Facilities
Indian Institute of Technology Kharagpur has a huge campus that spans over an area of 2100 acres. Being on equal footing with other old IITs across India, the college has a number of provisions available for students. Some of these facilities are as follows:  

Hostel: There are 21 halls of residence in total, 16 for boys and 5 for girls. The hostels have a high capacity of housing almost 10,000 students overall. All hostels have in-house eateries that serve delicious varieties of food from all regions of India. Facilities such as High-Speed LAN, Wi-Fi and 24-hour electricity is available to all residents.  
Food: Eateries are available in the hostels as well as in other areas across the campus. The tech market also has a wide variety of snacks and sweets that residents can buy.  
Sports: There are two stadiums on the campus, namely Jnan Ghosh and Tata Sports Complex for various games such as Hockey, Football and cricket. Apart from these, the campus also has a completely modernized Aquatic Center for sports like Swimming as well as Water Polo. The Gymkhana also hosts an Indoor Squash Court, Indoor badminton courts, pool tables, tennis courts, and a fully modernized Gymnasium, equipment and facilities for weightlifting, basketball courts, volleyball court, table tennis etc. 
Health Care: TheB.C Roy Technology Hospital is located centrally within the Indian Institute of Technology Kharagpur campus. The hospital features an ICU, OPD, 24x7 pharmacy, 32 beds, emergency ward and other necessities. The hospital staff is highly qualified and dedicated to providing round the clock medical attention to students, staff and faculty.  
Library: IIT Kharagpur has a Central Library which is one of the largest and finest technical libraries in Asia. The library is stocked with 3.5 lakh documents, 300 print journals as well as over 20,000 e-books. The library is accessible to all students, faculty and staff for academic and research purposes. ''')

    stat="https://www.shiksha.com/college/iit-kharagpur-indian-institute-of-technology-2999" #stats
    al="http://www.iitkgp.ac.in/admission" #admissions
    ow="http://www.iitkgp.ac.in/" #official site
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def IITGuwahati (): #IIT Guwahati
  print(''' Indian Institute of Technology Guwahati, the sixth member of the IIT fraternity, was established in 1994. The academic programme of IIT Guwahati commenced in 1995. At present the Institute has eleven departments and five inter-disciplinary academic centres covering all the major engineering, science and humanities disciplines, offering BTech, BDes, MA, MDes, MTech, MSc and PhD programmes. Within a short period of time, IIT Guwahati has been able to build up world class infrastructure for carrying out advanced research and has been equipped with state-of-the-art scientific and engineering instruments.Indian Institute of Technology Guwahati's campus is on a sprawling 285 hectares plot of land on the north bank of the river Brahmaputra around 20 kms. from the heart of the city. With the majestic Brahmaputra on one side, and with hills and vast open spaces on others, the campus provides an ideal setting for learning.
IIT Guwahati Ranking
Indian Institute of Technology Guwahati is one of the best institutes in India. Many reputed magazines and bodies have ranked IIT Guwahati:

Ranked 117 out of 650 top institutes of Asia by QS Asia Rankings 2021.
Ranked 7th in Engineering category by NIRF Ranking 2019
Ranked 10th nationally by QS Rankings 2020
Ranked 201-800 by Times Higher Education World University Rankings 2020
Ranked 6th by India Today Ranking 2019 
Ranked 7th in Engineering by Outlook Ranking 2019
Ranked 927th Internationally by US News Rankings 2020''')

  stat="https://collegedunia.com/university/25396-indian-institute-of-technology-iit-guwahati"  #stats and info 
  ow="https://www.iitg.ac.in/#"  #official website
  al="https://www.iitg.ac.in/admission/" #admissions
  print()
  print()
  print()
  i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
  l=[ow,al,stat]
  webbrowser.open(l[i-1])


def IITRoorkee (): #IIT Roorkee
    print (''' Vision
To attain global level of excellence in education and to create a sustainable and equitable society through innovative research in science and technology.

Mission
To create an environment that shall foster the growth of intellectually capable, innovative and entrepreneurial professionals, who shall contribute to the growth of Science and Technology in partnership with industry and develop and harness it for the welfare of the nation and mankind.

Core Values
Academic integrity and accountability
Respect and tolerance for the views of every individual
Attention to issues of national relevance as well as of global concern
Holistic understanding, including knowledge of the human sciences
Appreciation of intellectual excellence and creativity
An unfettered spirit of learning exploration, rationality and enterprise
Sensitivity to social responsibilities
About IIT Roorkee
Indian Institute of Technology - Roorkee is among the foremost of institutes of national importance in higher technological education and in engineering, basic and applied research. Since its establishment, the Institute has played a vital role in providing the technical manpower and know-how to the country and in pursuit of research. The Institute ranks amongst the best technological institutions in the world and has contributed to all sectors of technological development. It has also been considered a trend-setter in the area of education and research in the field of science, technology, and engineering.

The Institute had celebrated its Sesquicentennial in October 1996 and now completed more than 170 years of its existence. It was converted to IIT on September 21, 2001 by an Ordinance issued by the Government of India declared it as the nation’s seventh Indian Institute of Technology, an “Institution of National Importance”.

The Institute offers Bachelor's Degree courses in 10 disciplines of Engineering and Architecture and Postgraduate's Degree in 55 disciplines of Engineering, Applied Science, Architecture and planning. The Institute has facility for doctoral work in all Departments and Research Centres.

​The Institute admits students to B.Tech. and B.Arch. courses through the Joint Entrance Examination (JEE) conducted at various centres all over India.''')

    ow="https://www.iitr.ac.in/" #official site
    al="https://www.iitr.ac.in/admissions/pages/Freshers'_Special:_Main_Page.html"  #admissions
    stat="https://www.shiksha.com/college/indian-institute-of-technology-roorkee-3057"  #stats
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])



def IIMBangalore(): #IIM Bangalore
    print(''' Indian Institute of Management Bangalore (IIMB), established in 1973, is a top-ranked institute among all the IIMs in India. It offers management courses at PG and Doctoral level. NIRF 2020 ranked the institute at the number 2 position after IIM Ahmedabad. PGP is it's most sought after program globally. The Average placement package of the 2019 batch went as high as INR 25 Lacs per annum. 

Some of the notable alumni of IIM Bangalore are – K. Radhakrishnan (Ex-ISRO Chairman), Ravi Subramanium (Popular Author), Shehla Rashid (Indian Politician), Vega Tamotia (Indian Actress) and many more.

MBA Admissions 2020 has seen a double-digit increase as compared to past years.
IIMB offers degree-granting programs and a certificate program, Executive Education Programmes and specialized courses in areas such as entrepreneurship and public policy. Total of 6 programs are offered including Certificate program.
Eligibility: For Postgraduation Program, Graduation in any stream with 50% marks and for Doctoral Program, Postgraduation in relevant stream. Along with a valid score of relevant stream
The placements reaffirm IIM Bangalore’s status as one of the two or three pre-eminent B-Schools in India. There is a distinguished and special Training & Placement Cell which deals in all kinds of internships programs, seminars, and workshops related to the preparatory sessions or drills for the placement assistance of the students. The Placements session the year 2019 has got over with 100% Placement Track Record in 2 days with 411 students got 488 offers from many elite and reputed recruiters.

IIM Bangalore Facilities
Events: Students Celebration on the Republic Day 2019 The students at IIM Bangalore celebrated the Republic Day with full enthusiasm and patriotism. Starting with the National Flag hoisting ceremony by the Director of IIMB, Prof. G. Raghuram followed by the patriotic songs sung by the students and IIMB staff members, Play performance by the students added with a speech by the director at the end of the occasion.
Hostel: The spacious, beautiful and well-maintained hostel blocks provide single room accommodation to all students.
Library: Spacious and extremely well-stocked the library is regularly updated with the latest journals and newsletters. It also provides access to online databases like Bloomberg. Its services are subscribed to by working professionals too.
Computing Facilities: IIMB is the only fully Wi-Fi enabled campus amongst comparable institutes. The Computer Centre is available for use 24 hours. The printer facility is provided in the computer center as well as in the hostel blocks. High-speed Internet, highly resourceful intranet, sharing software, and internal messenger make all work easier and quicker.
Sports Room: With a strong focus on the overall development of the student's personality, IIMB has a robust sporting infrastructure. This includes facilities for tsepak, soccer, cricket, tennis, basketball, volleyball, throw ball, badminton, indoor games, etc. These facilities have had a role to play in the institute having a strong sporting culture.''')
    

    stat="https://collegedunia.com/university/25602-indian-institute-of-management-iimb-bangalore" #stats
    ow="https://www.iimb.ac.in/home" #official website
    al="https://www.iimb.ac.in/admissions" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def IIMAhmedabad (): #IIM Ahmedabad
    print (''' IIM Ahmedabad, established in the year 1961 is ranked 1 in NIRF 2020 ranking, 40th best institute in world and 6th best in Asia by QS World Ranking.  IIMA is an autonomous institution and offers Post-graduation, Diploma, Certificate, Executive, and fellowship Programs in Management. Currently,the most popular course at IIM Ahmedabad is Executive MBA (PGP-Ex), which is also rated in the top 5 courses by Financial Times in the world. Last year, a total of 881 students were enrolled out of which 237 were females. 

To be eligible for IIMA admission, one must have a valid score in CAT, GMAT, or GRE entrance exams. Last year, the percentile of CAT for IIM Ahmedabad reached up to 99.6. Apart from this, 75 companies visited the Institute for placement drive, out of which Amazon, Hindustan Unilever Limited and Amazon were the highest recruiters.
The flagship MBA program witnessed an increase in Arts Graduates from 3% to 5% in the academic session 2020. However, a decrease in the students intake from the Commerce and Science Streams was observed, in comparison to previous years.

MBA Admissions 2020 has seen a double-digit increase as compared to past years. To know what MBA course has to offer, click here

IIM Ahmedabad has also started an executive wing to cater the need of acquiring desired skills by the executives. This wing provides certificate as well as diploma courses for which candidate can apply online. ''')

    stat="https://collegedunia.com/university/25494-indian-institute-of-management-iima-ahmedabad?utm_source=home_RIGHT&utm_medium=7"#stats
    ow="https://www.iima.ac.in/"  #official site
    al="https://www.iima.ac.in/web/pgp/apply/domestic/admission/selection-process"  #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def NationalInstituteofTechnologyTiruchirappalli (): #National Institute of Technology, Tiruchirappalli
    print(''' National Institute of Technology Trichy (NITT) is situated in Tiruchirappalli division of Tamilnadu. It was established as a joint venture of the Govt. of Tamil Nadu and Govt. of India in 1964. NIT Trichy was formerly known as the Regional Engineering College, Tiruchirappalli. With the approval of the Government of India, NITT was granted Deemed University Status in 2003. NITT was ranked 11 by the National Institutional Ranking Framework in 2018. Since the very beginning, it has been imparting knowledge to various students from all over the country. The institute started with three engineering branches namely Civil, Mechanical and Electrical. For regulating the day-to-day work of the Institute, a large number of policy decisions, ordinances, regulations, rules, etc. have been formulated by the Senates and Board of Governors. 

NITT Trichy offers a total of 36 courses under 7 postgraduate and undergraduate degrees in the field of technology. These courses are administered by 18 departments of the college. More than 3,500 students of NITT are supervised and well thought of by 250 faculty members.

Spread over an area of 800 acres, NITT offers the students facilities to make their college life the best experience. Apart from well-equipped classrooms, laboratories, computer labs and more, it also has hostel facilities, medical facilities and even bank facilities at its best. It also provides its students with a reprographics centre, ATM, bookstall, co-op, canteen and a swimming pool. 22 boys’ and 5 girls’ hostels of NITT can accommodate up to 6000 undergraduate and postgraduate students. 

NIT Trichy has received “University of the year award” in the year 2017 by Federation of Indian Chambers of Commerce and Industry and "Best Industry linked National Institute of Technology in India" award by Confederation of Indian Industry in the year 2015.''')

    stat="https://www.collegedekho.com/colleges/nit-trichy" #stats
    ow="https://www.nitt.edu/"    #official site
    al="https://www.nitt.edu/home/admissions/"  #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])



def NITRourkela (): #NIT Rourkela
    print(''' Situated in the heart of Odisha, NIT Rourkela stands as a symbol of an educational mecca in the steel city of Rourkela. The Chain of National Institute of Technology or NITs including NIT Rourkela is a government-funded technological institution. NIT Rourkela is one of the most popular colleges for engineering courses. The college offers undergraduate, postgraduate and doctoral level courses in its campus. NIT Rourkela has a total of 44 courses taught in its Rourkela campus. The premium technological institution does not only have B.Tech and M.Tech level courses but also offers B.Sc+M.Sc, B.Tech+M.Tech and B.Arch courses.

NIT Rourkela has been modernized with the help of foreign collaborative funding agencies that are, the Material theme in the Materials and Metallurgical Engineering department under India - United Kingdom REC project and the Computer Science and Electronics streams which are under World Bank cum Swiss Development Corporation Project named IMPACT.

The city of Rourkela came to prominence after the establishment of Public Steel Plants in the area with collaboration with Germany in 1954-55. This is now a metropolitan city in Odisha. NIT Rourkela was established around the same time for boosting technological education in the newly built industrial city. NIT Rourkela is situated in the north-eastern corner of the city. The institute is easy to reach by road and by train. NIT Rourkela is located at a distance of approximately 6.7 kilometres distance from the nearest prominent railway station of Rourkela.''')


    ow="https://www.nitrkl.ac.in/"  #official site
    stat="https://www.collegedekho.com/colleges/national-institute-of-technology-rourkela" #stats
    al="https://nitrkl.ac.in/oldwebsite/Prospective_Students/2Admission/Default.aspx" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def LadyShriRamCollege (): #Lady Shri Ram College
    print(''' In the session 2018-19, 115 students got placed in the recruitment drive. The average salary package was 7.5 LPA and the highest salary package was 37.8 LPA. More than 100 companies participated in the recruitment drive. Many companies like Embibe, Musigma, Inmobi and start-ups like Indus Insights, Study Pad and Cogito Hub visited the campus for the first time. The key recruiters were Deloitte, Samsung, Bloomberg, Mckinsey & Company, KPMG and EY.

With the assistance of LSR-IQAC and Dr Renu Kaul, the teacher-in-charge, a 2-month long internship is provided at the Ministry of Statistics and Programme Implementation to the students of the Department of Statistics. Under the supervision SDG Monitoring Unit of Social Statistics Division, different projects were handed over to the students.

In the session 2018-19, more than 320 companies visited the college. The highest package offered for an internship was INR 1,50,000 for two months. Many companies like Standard Chartered, Amnesty International, Nomura, JSW, CitiBank, Yes Bank, Outlook Magazine and ED Times provided students opportunities for internships.''')
    stat="https://www.shiksha.com/college/lady-shri-ram-college-for-women-lajpat-nagar-delhi-23895"#stats
    ow="https://lsr.edu.in/" #official site
    al="https://lsr.edu.in/admissions/admission-procedure/"  #admission
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])


def LoyolaCollege (): #Loyola College
    print(''' Rankings
Ranked 6th Top College in India by NIRF 2019.
Elevated to the status of the college of excellence by UGC.
Reaccredited by NAAC with 3.70 CGPA out of 4.00.
Loyola College Courses
Loyola College has various courses offered through its eight departments and a research center. The departments are mentioned below:

School of Commerce and Economics
School of Computational Sciences
School of Physical Sciences
School of Vocational Studies
School of Humanities
School of Languages
School of Life Sciences
School of Media Studies
There are numerous facilities offered by the College for the overall development of the students. Few of them are mentioned below:

Hostels: Hostels are provided for boys and girls separately. Admission into hostels will be considered only after the admission into Loyola College. Only limited seats are available in the hostels. For further details, please contact the Hostel Administration.
Loyola Hostel for Men: 044-28178352
The Dean of Women Students processes the admission of girls into the hostel.
Loyola Women's Hostel: 044-28178452
Library: Students and Staff who are at present working or studying are eligible to become members of this library. Membership for outsiders is not allowed. In case non-members and past students want to make a short reference they shall meet the Library Director or Librarian for permission.
Health Center: LHC has dedicated general physicians, staff nurse and lab technicians available on all working days to administer free medical treatments to all staff and students.
Food Court: There are multiple food vendors offering a variety of cuisines with Local, national and international flavor to cater to the recipe of the students.''')
    
    
    stat="https://collegedunia.com/college/2595-loyola-college-chennai"  #stats
    ow="https://www.loyolacollege.edu/" #official site
    al="https://erp.loyolacollege.edu/loyolaonline/application/loginManager/youLogin.jsp" #admissions
    print()
    print()
    print()
    i=int(input("to visit official website press1, 2 for admission, 3 to know the statistics of the university"))
    l=[ow,al,stat]
    webbrowser.open(l[i-1])
    



  
    































































































    
