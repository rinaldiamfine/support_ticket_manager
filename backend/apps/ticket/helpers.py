from apps.ticket.models import (
    Tickets,
    TicketLines,
    # TicketStatus,
    # TicketCategories
)

class TicketHelpers:
    def __init__(self):
        pass

    def merge_tickets(self, datas: list):
        print("GOGOGO", datas)

    def get(self, values: dict):
        ticket_ids = Tickets.base_query().filter(
            
        ).all()
        return ticket_ids

    def create(self, values: dict):
        ticket_id = Tickets(
            name=values.get('name'),
            description=values.get('description'),
            user_id=values.get('user_id'),
            status_id=values.get('status_id'),
            category_id=values.get('category_id'),
        )
        ticket_id.save()
        return True, ticket_id
    
    def delete(self, ticket: int):
        ticket_id = Tickets.base_query().filter_by(
            id=ticket
        ).first()
        if not ticket_id:
            return False, "Ticket not found"
        ticket_id.delete()
        return True, ticket_id
    
    def update(self, values: dict):
        ticket_id = Tickets.base_query().filter(
            Tickets.id == values.get('id')
        ).first()
        if not ticket_id:
            return False, "Ticket not found"
        ticket_id.update(values)
        return True, ticket_id
