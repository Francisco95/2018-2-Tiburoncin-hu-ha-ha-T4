from django.db import models
from datetime import datetime


class User(models.Model):
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    rut = models.CharField(max_length=20, unique=True, primary_key=True)
    password = models.CharField(max_length=50)

    ADMIN = 'AD'
    NATURAL_PERSON = 'NP'
    USER_TYPE = (
        (ADMIN, 'Admin'),
        (NATURAL_PERSON, 'NaturalPerson'),
    )
    user_type = models.CharField(max_length=2, choices=USER_TYPE,
                                 default=NATURAL_PERSON,)

    def __str__(self):
        return "%s, %s" % (self.last_name, self.first_name)

    def not_admin(self):
        return self.user_type == self.NATURAL_PERSON


# class Course(models.Model):
#     code = models.IntegerField()
#     section_number = models.IntegerField(default=1)
#     year = models.IntegerField(default=datetime.now().year)
#
#     PRIMAVERA = 'Primavera'
#     OTONO = 'Otoño'
#     SEMESTER = (
#         (PRIMAVERA, PRIMAVERA),
#         (OTONO, OTONO),
#     )
#     semester = models.CharField(max_length=9, choices=SEMESTER)
#
#     def __str__(self):
#         return "%s-%s, %s %s" % (self.code, self.section_number,
#                                  self.semester, self.year)
#
#     class Meta:
#         unique_together = (('code', 'section_number', 'year', 'semester'),)
#
#
# class NamesPerCode(models.Model):
#     code = models.IntegerField()
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return "%s: %s" % (self.name, self.code)
#
#     class Meta:
#         unique_together = (('code', 'name'),)
#
#
# class Question(models.Model):
#     id = models.IntegerField(primary_key=True)
#     GRADE = 'Grade'
#     FREE = 'Free'
#     QUESTION_TYPE = (
#         (GRADE, GRADE),
#         (FREE, FREE),
#     )
#     question_type = models.CharField(max_length=5, choices=QUESTION_TYPE)
#     question = models.TextField()
#
#     def __str__(self):
#         return "%s: (type %s) %s" % (self.id, self.question_type, self.question[:10])
#
#
# class UserInCourse(models.Model):
#     member = models.ForeignKey(User, on_delete=models.CASCADE)
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#
#     PROFESOR = 'Profesor'
#     AUXILIAR_TEACHER = 'Profesor auxiliar'
#     AYUDANTE = 'Ayudante'
#     ESTUDIANTE = 'Estudiante'
#     ROL = (
#         (PROFESOR, PROFESOR),
#         (AUXILIAR_TEACHER, AUXILIAR_TEACHER),
#         (AYUDANTE, AYUDANTE),
#         (ESTUDIANTE, ESTUDIANTE),
#     )
#     rol = models.CharField(max_length=17, choices=ROL)
#
#     def __str__(self):
#         return "%s; %s (%s)" % (self.member, self.course, self.rol)
#
#     class Meta:
#         unique_together = (('member', 'course'),)
#
#
# class Group(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     member = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return "%s (%s): %s" % (self.name, self.course, self.member)
#
#     class Meta:
#         unique_together = (("course", "name"),)
#
#
# class CoEvaluation(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40, default='Co-evaluacion')
#     id = models.IntegerField(primary_key=True)
#
#     init_date = models.DateTimeField(default=datetime.now)
#     end_date = models.DateTimeField(default=datetime.max)
#
#     @property
#     def open(self):
#         return self.init_date < datetime.now() and not datetime.now() > self.end_date
#
#     def __str__(self):
#         return "%s, %s (%s - %s)" % (self.course, self.name, self.init_date, self.end_date)
#
#
# class UserActionOnCoEvaluation(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     co_evaluation = models.ForeignKey(CoEvaluation, on_delete=models.CASCADE)
#     date = models.DateTimeField(default=datetime.now)
#
#     ANSWER = 'Responde'
#     PUBLISH = 'Publica'
#     ACTION_TYPE = (
#         (ANSWER, ANSWER),
#         (PUBLISH, PUBLISH),
#     )
#     action_type = models.CharField(max_length=5, choices=ACTION_TYPE)
#
#     def __str__(self):
#         return "%s: %s %s on %s" % (self.user, self.action_type, self.co_evaluation, self.date)
#
#
# class AnswerQuestion(models.Model):
#     user_who_answer = models.ForeignKey(User, related_name="answer", on_delete=models.PROTECT)
#     user_related = models.ForeignKey(User, on_delete=models.PROTECT)
#     question = models.ForeignKey(Question, on_delete=models.PROTECT)
#     response = models.TextField()
#
#     def __str__(self):
#         return "%s response %s related to %s" % (self.user_who_answer,
#                                                  self.question, self.user_related)
#
#
# class QuestionsInCoEvaluation(models.Model):
#     co_evaluation = models.ForeignKey(CoEvaluation, on_delete=models.CASCADE)
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     weight = models.IntegerField(default=0)
#
#     def __str__(self):
#         return "%s: %s (weight=%s)" % (self.co_evaluation, self.question, self.weight)
#
#
# class UnlinkedCourse(models.Model):
#     user_in_course = models.ForeignKey(UserInCourse, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return "%s" % self.user_in_course
#
#
# class UnlinkedGroup(models.Model):
#     user_in_group = models.ForeignKey(Group, on_delete=models.PROTECT)
#
#     def __str__(self):
#         return "%s" % self.user_in_group
