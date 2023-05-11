
// DOCUMENTATION FOR THE COLORS
// ring-gray-500/10
// ring-red-600/10
// ring-yellow-600/20
// ring-green-600/20
// ring-blue-700/10
export function Badge(name, classType) {
    return (
        <>
            <span className={"inline-flex items-center rounded-md bg-red-50 px-2 py-1 text-xs font-medium text-red-700 ring-1 ring-inset" + classType}>
                { name }
            </span>
        </>
    )
}