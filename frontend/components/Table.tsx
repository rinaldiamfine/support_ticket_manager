import React from 'react'
import { Column, useTable } from 'react-table'
import { classNames } from './Utils'

// Define a default UI for filtering
// function GlobalFilter(
//     preGlobalFilteredRows: any,
//     globalFilter: any,
//     setGlobalFilter: any,
//     ) {
//     const count = preGlobalFilteredRows.length
//     const [value, setValue] = React.useState(globalFilter)
//     const onChange = useAsyncDebounce((value: any) => {
//       setGlobalFilter(value || undefined)
//     }, 200)
  
//     return (
//       <label className="flex gap-x-2 items-baseline">
//         <span className="text-gray-700">Search: </span>
//         <input
//           type="text"
//           className="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
//           value={value || ""}
//           onChange={e => {
//             setValue(e.target.value);
//             onChange(e.target.value);
//           }}
//           placeholder={`${count} records...`}
//         />
//       </label>
//     )
// }
  
  // This is a custom filter UI for selecting
  // a unique option from a list
// export function SelectColumnFilter(
//     column: { filterValue: string, setFilter: any, preFilteredRows: any, id: any, render: any }
// ) {
//     // Calculate the options for filtering
//     // using the preFilteredRows
//     const options = React.useMemo(() => {
//       const options = new Set()
//       preFilteredRows.forEach((row: { values: { [x: string]: unknown } }) => {
//         options.add(row.values[id])
//       })
//       return [...options.values()]
//     }, [id, preFilteredRows])
  
//     // Render a multi-select box
//     return (
//       <label className="flex gap-x-2 items-baseline">
//         <span className="text-gray-700">{render("Header")}: </span>
//         <select
//           className="rounded-md border-gray-300 shadow-sm focus:border-indigo-300 focus:ring focus:ring-indigo-200 focus:ring-opacity-50"
//           name={id}
//           id={id}
//           value={filterValue}
//           onChange={e => {
//             setFilter(e.target.value || undefined)
//           }}
//         >
//           <option value="">All</option>
//           {options.map((option, i) => (
//             <option key={i} value={option}>
//               {option}
//             </option>
//           ))}
//         </select>
//       </label>
//     )
// }
  
export function StatusPill(value: string) {
    const status = value ? value.toLowerCase() : "unknown";
  
    return (
      <span
        className={
          classNames(
            "px-3 py-1 uppercase leading-wide font-bold text-xs rounded-full shadow-sm",
            status.startsWith("active") ? "bg-green-100 text-green-800" : null,
            status.startsWith("inactive") ? "bg-yellow-100 text-yellow-800" : null,
            status.startsWith("offline") ? "bg-red-100 text-red-800" : null,
          )
        }
      >
        {status}
      </span>
    );
};
  
export function AvatarCell(value: string, column: any, row: any) {
    return (
      <div className="flex items-center">
        <div className="flex-shrink-0 h-10 w-10">
          {/* <img className="h-10 w-10 rounded-full" src={row.original[column.imgAccessor]} alt="" /> */}
        </div>
        <div className="ml-4">
          <div className="text-sm font-medium text-gray-900">{value}</div>
          {/* <div className="text-sm text-gray-500">{row.original[column.emailAccessor]}</div> */}
        </div>
      </div>
    )
}

function Table({ columns , data }) {
    const { getTableProps, getTableBodyProps, headerGroups, rows, prepareRow } =
    useTable({
      columns,
      data,
    });

    return (
        <table {...getTableProps()}>
            <thead>
                { headerGroups.map((headerGroup: { getHeaderGroupProps: () => { [x: string]: any; key: any; }; headers: any[]; }) => {
                const { key, ...restHeaderGroupProps } =
                    headerGroup.getHeaderGroupProps();
                return (
                    <tr key={key} {...restHeaderGroupProps}>
                    {headerGroup.headers.map((column) => {
                        const { key, ...restColumn } = column.getHeaderProps();
                        return (
                        <th key={key} {...restColumn}>
                            {column.render("Header")}
                        </th>
                        );
                    })}
                    </tr>
                );
                }) }
            </thead>
            <tbody {...getTableBodyProps}>
                { rows.map((row: { getRowProps: () => { [x: string]: any; key: any; }; cells: any[]; }) => {
                prepareRow(row);
                const { key, ...restRowProps } = row.getRowProps();
                return (
                    <tr key={key} {...restRowProps}>
                    {row.cells.map((cell) => {
                        const { key, ...restCellProps } = cell.getCellProps();
                        return (
                        <td key={key} {...restCellProps}>
                            {cell.render("Cell")}
                        </td>
                        );
                    })}
                    </tr>
                );
                }) }
            </tbody>
        </table>
      );
  }
  
  export default Table;