

export type TicketModel = {
    id: string,
    created: string,
    updated: string,
    user_id: string,
    user_name: string,
    description: string,
    category_id: string,
    category_name: string,
    status_id:string,
    status_name: string
}

export type TicketLineModel = {
    id: string,
    ticket_id: string,
    created: string,
    updated: string,
    user_id: string,
    user_name: string,
    description: string
}
