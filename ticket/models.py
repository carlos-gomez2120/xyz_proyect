from django.db import models
from persons.models import Person
from tax.models import TaxPriceProduct

"""
    Modelos relacionados con ticket:
        -ticket
        -ticketDetail
"""


class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    ticket_date = models.DateField()
    half_payment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fk_id_person_cashier = models.ForeignKey(Person, models.DO_NOTHING, db_column='fk_id_person_cashier', related_name='fk_id_person_cashier')
    fk_id_person_customer = models.ForeignKey(Person, models.DO_NOTHING, db_column='fk_id_person_customer', related_name='fk_id_person_customer')

    class Meta:
        managed = True
        db_table = 'ticket'


class TicketDetail(models.Model):
    id_ticket_detail = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    devolution_request = models.DateField(blank=True, null=True)
    devolution_approved = models.DateField(blank=True, null=True)
    description_devolution = models.CharField(max_length=45, blank=True, null=True)
    fk_id_tax_price_product = models.ForeignKey(TaxPriceProduct, models.DO_NOTHING, db_column='fk_id_tax_price_product')
    fk_id_ticket = models.ForeignKey(Ticket, models.DO_NOTHING, db_column='fk_id_ticket')
    fk_id_person_administrator = models.ForeignKey(Person, models.DO_NOTHING, db_column='fk_id_person_administrator', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ticket_detail'
