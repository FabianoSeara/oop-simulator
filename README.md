# Container Yard Simulator (OOP)

A small simulation of a container yard that assigns handling equipment
(RTG / RS) to incoming trucks, with a FIFO waiting queue and a service
report.

## How to run

py main.py



Expected output: two trucks initially wait, the report shows 3 attended
and 2 waiting with an average of 25.0 min. Releasing an RTG serves Tiago
(4 attended, 1 waiting, 31.2 min avg). Releasing an RS serves Jack
(5 attended, 0 waiting, 30.0 min avg).

## Project layout

- `classes.py` — models and business rules:
  - `Truck` — a truck; computes its own `departure_time` from
    `arrival_time + service_duration`
  - `Equipment` — a piece of equipment; knows how to `occupy(truck)`
    and `release()` itself
  - `Yard` — the yard: owns the fleet (`equipment_list`), the FIFO
    queue (`waiting`) and the history of every truck that entered
    (`all_trucks`). Orchestrates `add_truck`, `release_equipment`
    and `print_report`
  - `find_available_equipment` / `process_truck` — helper functions
- `main.py` — builds the scenario and runs the simulation
- `test_simulator.py` — minimal assert-based test of the core flow

## Rules

- Each truck requires a given equipment type (`RTG` or `RS`).
- If a free equipment of the right type exists, the truck occupies it
  and leaves at `departure = arrival + service_duration` (minutes).
- Otherwise the truck is appended to the end of the waiting queue.
- When an equipment is released, the first truck in the queue that
  needs that type is served. One release serves one truck.

## Design notes (OOP vs. dictionary version)

- Attribute access uses dots (`item.equipment_type`) instead of
  subscripts (`item["type"]`).
- Releasing an equipment is a method on the object
  (`equipment.release()`) instead of a standalone function taking an
  id and the whole list — the object *is* the one being changed, so
  no lookup is needed.
- `find_equipment_by_id` is gone: the `Yard` owns the fleet, so no
  global list traversal is required.
- Shared state (fleet + queue) lives on `Yard`, not in loose module
  variables. This is what makes the "waiting" state survive between
  events — previously the waiting truck was printed but lost.

## Tests

py test_simulator.py



Plain asserts, no framework. Covers allocation when equipment is free,
queuing when it is not, and FIFO dispatch on `release_equipment`.
Prints `Ok` on success.