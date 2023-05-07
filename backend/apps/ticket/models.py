from apps.tools.base_model import BaseModel
from sqlalchemy.orm import relationship
import sqlalchemy as sa
from apps import db

class TicketStatus(BaseModel):
    __tablename__ = 'ticket_status'

    code = sa.Column(sa.String(50), nullable=False)
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text())
    ticket_status_ids = relationship("Tickets", back_populates="status")

    def __repr__(self):
        return '<id : %s>' % (self.id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def add_flush(self):
        try:
            db.session.add(self)
            db.session.flush()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

class TicketCategories(BaseModel):
    __tablename__ = 'ticket_categories'

    code = sa.Column(sa.String(50), nullable=False)
    name = sa.Column(sa.String(50), nullable=False)
    description = sa.Column(sa.Text())
    ticket_category_ids = relationship("Tickets", back_populates="category")

    def __repr__(self):
        return '<id : %s>' % (self.id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def add_flush(self):
        try:
            db.session.add(self)
            db.session.flush()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

class Tickets(BaseModel):
    __tablename__ = 'tickets'

    user_id = sa.Column(sa.Integer(), nullable=False)
    name = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text())
    status_id = sa.Column(sa.Integer(), sa.ForeignKey('ticket_status.id', ondelete='CASCADE'), nullable=False)
    status = relationship("TicketStatus", back_populates="ticket_status_ids")
    category_id = sa.Column(sa.Integer(), sa.ForeignKey('ticket_categories.id', ondelete='CASCADE'), nullable=False)
    category = relationship("TicketCategories", back_populates="ticket_category_ids")
    ticket_ids = relationship("TicketLines", back_populates="ticket")

    def __repr__(self):
        return '<id : %s>' % (self.id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def add_flush(self):
        try:
            db.session.add(self)
            db.session.flush()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

class TicketLines(BaseModel):
    __tablename__ = 'ticket_lines'

    user_id = sa.Column(sa.Integer(), nullable=False)
    ticket_id = sa.Column(sa.Integer(), sa.ForeignKey('tickets.id', ondelete='CASCADE'), nullable=False)
    ticket = relationship("Tickets", back_populates="ticket_ids")
    description = sa.Column(sa.Text())

    def __repr__(self):
        return '<id : %s>' % (self.id)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def add_flush(self):
        try:
            db.session.add(self)
            db.session.flush()
            return self

        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
            return True

        except Exception as e:
            db.session.rollback()
            raise Exception(e)
