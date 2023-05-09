from apps.ticket.models import (
    Tickets,
    TicketLines,
    TicketStatus,
    TicketCategories
)
from apps.ticket.schemas import (
    TicketSchema,
    TicketListSchema
)
import os
import pandas as pd


class TicketCategoryHelpers:
    def __init__(self) -> None:
        self.base_path = os.getenv('BASE_PATH')

    def seed_ticket_categories(self):
        seeder_path = os.path.join(self.base_path, 'apps', 'seeders')
        ticket_category_path = os.path.join(seeder_path, 'ticket_category.csv')
        
        data = pd.read_csv(ticket_category_path)
        df = pd.DataFrame(data)
        for row in df.itertuples():
            ticket_ids = TicketCategories.base_query().filter(
                TicketCategories.code == row.code
            ).all()
            if len(ticket_ids)>0:
                print(f"- The ticket category with code:{row.code} is already exist on database!")
                continue
            
            ticket_category_id = TicketCategories(
                code=row.code,
                name=row.name,
                description=row.description,
            )
            ticket_category_id.save()

        print("Finishing seed the ticket category process!\n")

class TicketStatusHelpers:
    def __init__(self) -> None:
        self.base_path = os.getenv('BASE_PATH')

    def seed_ticket_status(self):
        seeder_path = os.path.join(self.base_path, 'apps', 'seeders')
        ticket_status_path = os.path.join(seeder_path, 'ticket_status.csv')
        
        data = pd.read_csv(ticket_status_path)
        df = pd.DataFrame(data)
        for row in df.itertuples():
            ticket_ids = TicketStatus.base_query().filter(
                TicketStatus.code == row.code
            ).all()
            if len(ticket_ids)>0:
                print(f"- The ticket status with code:{row.code} is already exist on database!")
                continue
            
            ticket_status_id = TicketStatus(
                code=row.code,
                name=row.name,
                description=row.description,
            )
            ticket_status_id.save()

        print("Finishing seed the ticket status process!\n")

class TicketHelpers:
    def __init__(
        self,
        api=None,
        method=None,
        user_id=None
    ):
        self.api = api
        self.method = method
        self.user_id = user_id

    def merge_tickets(self, datas: list):
        print("GOGOGO", datas)

    def list(self, values: dict):
        ticket_ids = Tickets.base_query().filter(
            
        ).all()
        result_dump = TicketSchema(many=True).dump(ticket_ids)
        result = TicketListSchema().load(
            {
                "ticket": result_dump,
                "limit": values.get('limit'),
                "offset": values.get('offset'),
                "keywords": values['keywords'] if values.get('keywords') else '',
                "total": len(ticket_ids)
            }
        )
        return result

    def create(self, values: dict):
        ticket_id = Tickets(
            name=values.get('name'),
            description=values.get('description'),
            user_id=values.get('user_id'),
            status_id=values.get('status_id'),
            category_id=values.get('category_id'),
        )
        ticket_id.save()
        return ticket_id
    
    def delete(self, id: int, user_id: int):
        ticket_id = Tickets.base_query().filter_by(
            id=id,
            user_id=user_id,
        ).first()
        if not ticket_id:
            return False, "Ticket not found"
        ticket_id.delete()
        return True, ticket_id
    
    def update(self, values: dict):
        ticket_id = Tickets.base_query().filter(
            Tickets.id == values.get('id'),
            Tickets.user_id == values.get('user_id')
        ).first()
        if not ticket_id:
            return False, "Ticket not found"
        print(values)
        ticket_id.update(**values)
        return ticket_id
