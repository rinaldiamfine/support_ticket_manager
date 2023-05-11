import React from "react"

export type ListModel = {
    id: string,
    subject: string,
    name: string,
    email: string,
    imageURL: any,
    status_id: string,
    status_name: string
}

export function List(datas: ListModel[], isUseImage: boolean) {
    return (
        <ul role="list" className="divide-y divide-gray-200">
            {datas.map((data) => (
                <li key={data.id} className="flex justify-between gap-x-6 py-5">
                    <div className="flex gap-x-4">
                        { isUseImage == true ? (
                         data.imageURL != null ? (
                            <img className="h-12 w-12 flex-none rounded-full bg-gray-50" src={data.imageURL} alt="" /> ) : <div className="h-12 w-12 flex-none rounded-full bg-white"/>
                        ) : "" }
                        <div className="min-w-0 flex-auto">
                            <p className="text-sm font-semibold leading-6 text-gray-900">{data.name}</p>
                            <p className="mt-1 truncate text-xs leading-5 text-gray-500">{data.email}</p>
                        </div>
                    </div>
                    <div className="flex gap-x-4">
                        <div className="min-w-0 flex-auto">
                            <p className="text-sm font-semibold leading-6 text-gray-900">{data.subject}</p>
                        </div>
                    </div>

                    {/* <div className="hidden sm:flex sm:flex-col sm:items-end">
                        <p className="text-sm leading-6 text-gray-900">{data.role}</p>
                        {data.lastSeen ? (
                        <p className="mt-1 text-xs leading-5 text-gray-500">
                            Last seen <time dateTime={data.lastSeenDateTime}>{data.lastSeen}</time>
                        </p>
                        ) : (
                        <div className="mt-1 flex items-center gap-x-1.5">
                            <div className="flex-none rounded-full bg-emerald-500/20 p-1">
                            <div className="h-1.5 w-1.5 rounded-full bg-emerald-500" />
                            </div>
                            <p className="text-xs leading-5 text-gray-500">Online</p>
                        </div>
                        )}
                    </div> */}
                </li>
            ))}
        </ul>
    )
}