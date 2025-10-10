import React from 'react'
import { Outlet } from 'react-router'

export default function footer() {
  return (
    <div>
      <b>footer</b>
      <Outlet />
    </div>
  )
}
