#!/usr/bin/env python
# coding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from apps import app, db, celery
# from noah.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

## To check the celery worker:
# celery -A noah.celery worker --loglevel=info

@manager.command
def celery_status():
    """
    This method used to check celery worker status
    """
    i = celery.control.inspect()
    availability = i.ping()
    stats = i.stats()
    registered_tasks = i.registered()
    active_tasks = i.active()
    scheduled_tasks = i.scheduled()
    result = {
        'availability': availability,
        'stats': stats,
        'registered_tasks': registered_tasks,
        'active_tasks': active_tasks,
        'scheduled_tasks': scheduled_tasks
    }
    return result

@manager.command
def seed_database():
    from apps.ticket.helpers import (
        TicketStatusHelpers,
        TicketCategoryHelpers
    )
    print("Seeding the ticket status")
    TicketStatusHelpers().seed_ticket_status()
    print("Seeding the ticket category")
    TicketCategoryHelpers().seed_ticket_categories()

@manager.command
def test():
    from apps.ticket.helpers import TicketHelpers
    from apps.openai.helpers import OpenAIHelpers
    # t = TicketHelpers()
    # t.merge_tickets(
    #     [{1, 'a'}, {2, 'b'}]
    # )
    
    o = OpenAIHelpers()
    # model = o.get_models()
    # print(model)

    print(o.min_prob, type(o.min_prob))
    # test = o.test_merge_ticket()
    # print(test)

@manager.command
def ticket():
    from apps.ticket.helpers import TicketHelpers
    t = TicketHelpers()
    s = t.get({'id': 10})
    print(s)

if __name__ == '__main__':
    manager.run()
