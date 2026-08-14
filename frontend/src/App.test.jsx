import { render, screen, waitFor } from '@testing-library/react'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'
import App from './App'

// --- Current behavior: static heading ----------------------------------------

describe('App (current behavior)', () => {
  it('renders a heading on the page', () => {
    render(<App />)
    expect(screen.getByRole('heading')).toBeInTheDocument()
  })
})

// --- PRD target behavior: fetch greeting from backend and display it --------
// These encode PRD.md's functional requirements ("On page load, the frontend
// calls the backend API to fetch the greeting message" / "The frontend
// displays 'Hola!!' on the screen"). They will fail until App.jsx actually
// fetches from the backend on mount — remove `.fails` at that point.

describe('App (PRD target behavior)', () => {
  beforeEach(() => {
    global.fetch = vi.fn()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it.fails('calls the backend /hola endpoint on mount', async () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: 'Hola MADHURI DASH!!' }),
    })

    render(<App />)

    await waitFor(() => {
      expect(fetch).toHaveBeenCalledWith(expect.stringContaining('/hola'))
    })
  })

  it.fails('renders the greeting message returned by the backend', async () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: 'Hola MADHURI DASH!!' }),
    })

    render(<App />)

    expect(await screen.findByText('Hola MADHURI DASH!!')).toBeInTheDocument()
  })

  it.fails('attempts the fetch and does not crash when it fails', async () => {
    fetch.mockRejectedValueOnce(new Error('Network error'))

    render(<App />)

    await waitFor(() => {
      expect(fetch).toHaveBeenCalledTimes(1)
    })
  })

  it.fails('only calls the backend once per mount', async () => {
    fetch.mockResolvedValueOnce({
      ok: true,
      json: async () => ({ message: 'Hola MADHURI DASH!!' }),
    })

    render(<App />)

    await waitFor(() => expect(fetch).toHaveBeenCalledTimes(1))
  })
})
