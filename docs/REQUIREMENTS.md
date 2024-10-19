# Project Context and Requirements Document: Coffee Roaster Control System
This document outlines the hardware specifications, functional and non-functional requirements, learnings from previous signal analysis, project milestones, and technical approaches to controlling the TRIAC for a coffee roaster heater using a Raspberry Pi 3B. This serves as a guide for structuring the project effectively as it progresses.

## 1. Hardware Specifications
1.1. Coffee Roaster:
Heater: 220-240V, 100W controlled via a TRIAC.
Fan: Independently controlled, basic inverted PWM control (100% duty cycle = 0% fan power).
Control Boards:
Internal Board: Handles AC mains power, TRIAC triggering, and power distribution.
External Controller Board: Provides user interface with dials and buttons for heat level, fan control, and timers. Detects zero cross on input wire from Internal Board, and times heater phase timing to TRIAC
Connection between boards: 6 pin header on Internal Board, 6 pin header on controller Board. Pins are labeled and color coded as follows:
Red - 5v power to external control board
Black - ground
Brown - "heat" control signal from controller board to internal board
Blue  - "fan" control signal from controller board to internal board
Yellow - "zero" provides 50hz AC signal from internal board to controller board
Green - "NTC" provides some pulses at startup and mode changes. Not sure of exact purpose.


1.2. Control Hardware:
Primary Controller: Raspberry Pi model 3B

CPU: ARM Cortex-A53, quad-core
GPIO: Sufficient GPIO pins for zero-cross detection, TRIAC triggering, and communication modules.
OS: Raspberry Pi OS (Debian-based)
Libraries: pigpio, RPi.GPIO, or specialized libraries for phase control as required.

Additional Components:

Logic Analyzer: For debugging and verifying signals.
Oscilloscope: For debugging and verifying signals.

## 2. Functional Requirements
Precise Heater Control:

Implement phase angle control to adjust power delivered to the heater.
Synchronize the TRIAC trigger signals with zero-crossing detection to minimize noise and ensure stability.
Allow users to control heater and fan manually, starting a roast, exectuing the cooldown cycle, and incrementing both heat and fan settings separately.

User Profile Management:

Create, save, and execute custom roasting profiles that specify heat and fan settings and cooldown commencement over time.
Profiles should be adjustable via an iOS app or local interface (to be developed).

Safety Mechanisms:

Implement safety checks to ensure that the heater and fan do not exceed operational limits.
System should handle error states gracefully, such as loss of zero-cross signal or hardware malfunctions.

## 3. Non-Functional Requirements
Performance:

The system must respond to zero-crossing signals in real-time, with minimal lag in triggering TRIACs.
Ensure accurate and repeatable control to maintain consistent roast quality.

Reliability:

Robust error handling and fail-safes must be in place to prevent system failures during operation.
System must be resilient to power fluctuations or unexpected inputs.

Scalability:

The architecture should allow easy additions of new sensors, control inputs, or integration with external applications.

Usability:

The system should have a simple user interface that allows easy adjustments of roast profiles and real-time feedback.
App integration should provide a seamless experience for creating and adjusting profiles.

## 4. Learnings from Logic Analyzer:

### Zero-Cross Signal Characteristics:

The zero-cross signal shows consistent 50Hz square wave behavior, confirming its role as the phase reference for the heater control.

### Heater Control Signal Observations:

Control signal patterns suggest synchronization with the zero-crossing, with short, consistent pulses indicating phase control.

Inverted heat and fan signals
Both heat and fan signals were observed to be inactive at "high" voltage. The fan is a simple PWM signal, where the duty cycle is varied to control the fan speed. 0% duty cycle corresponded to 100% fan power, and 100% duty cycle switches the fan off.
The heater signalling is a phase shifted pulse that occurs a precise time after the zero-cross is detected. The pulse is observed as a change from high to low, EG inverted

### Irregular AC Waveform Period:

Observed 9-11 ms variations in the period indicate possible instability in the power source or measurement noise, which should be addressed for accurate control.


## 5. Project Milestones

### Milesone 0: Development environment set up connection to pi verified

The plan is to develop locally in Cursor, using rclone to mount the raspberry pi to the local file system. Changes will be made via cursor, and then exectuted and tested in the pi using warp terminal.

### Milestone 0: Development environment setup and connection to Pi verified

The plan is to develop locally in Cursor, using rclone to mount the Raspberry Pi's filesystem locally. Changes will be made via Cursor, and then executed and tested on the Pi using Warp terminal.

Setup steps:
1. Ensure the Raspberry Pi and development machine are on the same local network.
2. Assign a static IP to the Raspberry Pi (e.g., 192.168.0.95).
3. Configure rclone for direct connection:
   a. Run `rclone config` on the development machine.
   b. Create a new remote named 'pi' using SFTP protocol.
   c. Use the Pi's static IP as the host.
   d. Set the user to 'kentboehm' and use SSH key authentication.
4. Test the connection with: `rclone ls pi:/home/kentboehm`
5. Mount the Pi's filesystem:
   ```
   rclone mount pi:/home/kentboehm /Users/kentboehm/raspberry_pi_mount --vfs-cache-mode writes &
   ```
6. Verify the mount in Cursor's sidebar.

This setup needs to be tested to ensure reliable connection and file synchronization.

### Milestone 1: System Setup and Signal Verification 

Set up Raspberry Pi, connect to roaster’s internal board, and verify zero-cross detection and TRIAC control using logic analyzer.
Test baseline scripts for zero-cross detection and basic TRIAC triggering.

### Milestone 2: Implement Basic TRIAC Control 

Develop and test scripts for burst firing and phase control.
Verify consistency and accuracy of control signals.

### Milestone 3: Profile Management and iOS App Integration 

Implement basic app functionality to create and send profiles to the control system.
Test communication between app and Raspberry Pi.

### Milestone 4: Full System Integration and Testing 

Integrate all system components and conduct end-to-end testing with user-defined profiles.
Perform stress tests, safety checks, and error handling evaluations.

### Milestone 5: Final Validation and User Feedback 

Collect feedback on usability and performance.
Refine software and hardware based on feedback and test results.


## 6. Technical Approach to TRIAC / Heater Control
Control Method: Burst firing synchronized with zero-cross detection for reliable power modulation.
Signal Processing: Use pigpio or similar libraries to handle zero-cross interrupts and generate precise timing delays for TRIAC triggering.
Safety Mechanisms: Implement software checks to monitor signal stability and hardware state.

## 7. Recommended Project Architecture
Project Structure:

bash
Copy code
/project-root
|-- /src
|   |-- main.py               # Main script to run the control system
|   |-- zero_cross.py         # Handles zero-cross detection and timing
|   |-- triac_control.py      # Functions for TRIAC triggering
|   |-- profile_manager.py    # Manages roasting profiles
|   |-- safety_checks.py      # Implements safety and error handling
|
|-- /config
|   |-- settings.json         # Configuration files for hardware settings
|
|-- /logs
|   |-- system.log            # Logs for debugging and performance analysis
|
|-- /docs
    |-- requirements.md       # Project requirements document
    |-- user_guide.md         # Instructions and user manual
Coding Standards:

Use Python with clear documentation and comments for all functions.
Include error logging to trace issues during operation.


## 8. Other Relevant Information
Debugging and Validation: Utilize logic analyzers and oscilloscopes regularly to validate timing and signal integrity.
Version Control: Use Git for code versioning, ensuring changes can be tracked, and revert if needed.
Testing Procedures: Set up automated tests for the control scripts to validate trigger timing against known good states.
This document serves as a comprehensive guide to initiate and manage the project, ensuring all key aspects are covered from hardware setup to software integration and control logic refinement.

### Development Workflow

1. Mount the Raspberry Pi filesystem using rclone:
   ```
   rclone mount pi:/home/kentboehm /Users/kentboehm/raspberry_pi_mount --vfs-cache-mode writes &
   ```
2. Open the mounted directory in Cursor IDE.
3. Develop and test directly on the mounted filesystem.
4. Use Warp terminal for executing commands on the Pi.
5. Commit changes regularly using Git.
6. Periodically create local backups for offline work or redundancy.