import { InternalLayout } from '@/components/Layout'
import { List, ListModel } from '@/components/List'

const people: ListModel[] = [
  {
    id: '1',
    name: 'Leslie Alexander',
    email: 'leslie.alexander@example.com',
    imageURL: null
  },
  {
    id: '2',
    name: 'Michael Foster',
    email: 'michael.foster@example.com',
    imageURL: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
  },
  {
    id: '3',
    name: 'Dries Vincent',
    email: 'dries.vincent@example.com',
    imageURL: null
  }
]

export default function Dashboard() {
  return (
    <InternalLayout>
      <header className="bg-white shadow">
        <div className="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold tracking-tight text-gray-900">Dashboard</h1>
        </div>
      </header>
      <main>
        <div className="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
          { List(people, true) }
        </div>
      </main>
    </InternalLayout>
  )
}
