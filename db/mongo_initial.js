/* Create the REGIE database and collections needed to store information */
use REGIE
db.dropDatabase();
use REGIE

db.createCollection("Course_Faculty")
db.createCollection("Course_Student")
db.createCollection("Faculty_Course")
db.createCollection("Student_Course")
db.createCollection("Request")
db.createCollection("Waitlist")

/* Insert initial data into the REGIE database */
db.Course_Faculty.insertMany([{_id: "MPCS_51410", faculty: [10000000]},
                              {_id: 'MPCS_52553', faculty: [20000000,40000000]},
                              {_id: 'PPHA_36800', faculty: [30000000]},
                              {_id: 'CAPP_30300', faculty: [50000000]},
                              {_id: 'MPCS_55001', faculty: [60000000,70000000]}])

db.Course_Student.insertMany([{_id: "MPCS_51410", student: [10000000,20000000,40000000,50000000]},
                              {_id: 'MPCS_52553', student: [10000000,30000000,50000000]},
                              {_id: 'PPHA_36800', student: [10000000,20000000,30000000,40000000,50000000]},
                              {_id: 'CAPP_30300', student: [10000000,40000000]},
                              {_id: 'MPCS_55001', student: [10000000,60000000]}])

db.Faculty_Course.insertMany([{_id: 10000000, course: ["MPCS_51410"]},
                              {_id: 20000000, course: ['MPCS_52553']},
                              {_id: 30000000, course: ['PPHA_36800']},
                              {_id: 40000000, course: ['MPCS_52553']},
                              {_id: 50000000, course: ['CAPP_30300']},
                              {_id: 60000000, course: ['MPCS_55001']},
                              {_id: 70000000, course: ['MPCS_55001']}])

db.Student_Course.insertMany([{_id: 10000000, course: ['MPCS_51410','MPCS_52553','PPHA_36800','CAPP_30300','MPCS_55001']},
                              {_id: 20000000, course: ['MPCS_52553','PPHA_36800']},
                              {_id: 30000000, course: ['MPCS_52553','PPHA_36800']},
                              {_id: 40000000, course: ['MPCS_51410','PPHA_36800','CAPP_30300']},
                              {_id: 50000000, course: ['MPCS_51410','MPCS_52553','PPHA_36800']},
                              {_id: 60000000, course: ['MPCS_55001']}])