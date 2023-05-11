import { InternalLayout } from '@/components/Layout'
import { List, ListModel } from '@/components/List'

const people: ListModel[] = [
  {
    id: '1',
    name: 'Leslie Alexander',
    email: 'leslie.alexander@example.com',
  },
  {
    id: '2',
    name: 'Michael Foster',
    email: 'michael.foster@example.com',
  },
  {
    id: '3',
    name: 'Dries Vincent',
    email: 'dries.vincent@example.com',
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
          { List(people) }
        </div>
      </main>
    </InternalLayout>
  )
}
