import React from 'react'
import { InternalLayout } from '@/components/Layout'
import { List, ListModel } from '@/components/List'
import TicketTable, { AvatarCell, StatusPill } from '@/components/TicketTable'
import './style.css'

const people: ListModel[] = [
  {
    id: '1',
    subject: "Asking for the lorem ipsum",
    name: 'Leslie Alexander',
    email: 'leslie.alexander@example.com',
    imageURL: null,
    type: "Hardware",
    type_id: "1",
    status: "Pending",
    status_id: "1"
  },
  {
    id: '2',
    subject: "Asking for the lorem ipsum",
    name: 'Leslie Alexander',
    email: 'leslie.alexander@example.com',
    type: "Hardware",
    type_id: "1",
    status: "Pending",
    status_id: "1",
    imageURL: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
  },
  {
    id: '3',
    subject: "Asking for the lorem ipsum",
    name: 'Leslie Alexander',
    email: 'leslie.alexander@example.com',
    imageURL: null,
    type: "Hardware",
    type_id: "1",
    status: "Pending",
    status_id: "1"
  }
]

const getData = () => [
  {
    name: "Jane Cooper",
    email: "jane.cooper@example.com",
    title: "Regional Paradigm Technician",
    department: "Optimization",
    status: "Active",
    role: "Admin",
    imgUrl:
      "https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
  },
  {
    name: "Cody Fisher",
    email: "cody.fisher@example.com",
    title: "Product Directives Officer",
    department: "Intranet",
    status: "Active",
    role: "Owner",
    imgUrl:
      "https://images.unsplash.com/photo-1570295999919-56ceb5ecca61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
  },
  {
    name: "Esther Howard",
    email: "esther.howard@example.com",
    title: "Forward Response Developer",
    department: "Directives",
    status: "Active",
    role: "Member",
    imgUrl:
      "https://images.unsplash.com/photo-1520813792240-56fc4a3765a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
  },
  {
    name: "Jenny Wilson",
    email: "jenny.wilson@example.com",
    title: "Central Security Manager",
    department: "Program",
    status: "Active",
    role: "Member",
    imgUrl:
      "https://images.unsplash.com/photo-1498551172505-8ee7ad69f235?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
  },
  {
    name: "Kristin Watson",
    email: "kristin.watson@example.com",
    title: "Lean Implementation Liaison",
    department: "Mobility",
    status: "Active",
    role: "Admin",
    imgUrl:
      "https://images.unsplash.com/photo-1532417344469-368f9ae6d187?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
  },
  {
    name: "Cameron Williamson",
    email: "cameron.williamson@example.com",
    title: "Internal Applications Engineer",
    department: "Security",
    status: "Active",
    role: "Member",
    imgUrl:
      "https://images.unsplash.com/photo-1566492031773-4f4e44671857?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=4&w=256&h=256&q=60",
  },
];

export default function Dashboard() {

  const columns = React.useMemo(() => [
    {
      Header: "Name",
      accessor: "name",
      imgAccessor: "imgUrl",
      emailAccessor: "email",
      Cell: AvatarCell
    },
    {
      Header: "Title",
      accessor: "title",
    },
    {
      Header: "Status",
      accessor: "status",
      Cell: StatusPill
    },
    {
      Header: "Role",
      accessor: "role",
    },
  ], [])

  const data = React.useMemo(() => getData(), []);

  // REQUEST API
  const [tickets, setTickets] = React.useState([])
  const fetchTicketData = () => {
      fetch('https://jsonplaceholder.typicode.com/posts')
      .then(response => { 
          return response.json()
      })
      .then(data => {
        setTickets(data)
      })
  }
  React.useEffect(() => {
    fetchTicketData()
  }, [])


  return (
    // <div>
    //   { tickets.length > 0 && (
    //     <ul>
    //       {tickets.map(user => (
    //         <li key={user.title}>{user.body}</li>
    //       ))}
    //     </ul>
    //   ) }
    // </div>

    <InternalLayout>
      <div className="min-h-screen bg-gray-100 text-gray-900 pt-4 pb-4">
        <main className="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8 pt-4 pb-4">
          <div className="">
              <h1 className="text-xl font-semibold">Tickets</h1>
          </div>
          <div className="mt-6">
            <TicketTable columns={columns} data={data} />
          </div>
        </main>
      </div>
    </InternalLayout>
  )
}
