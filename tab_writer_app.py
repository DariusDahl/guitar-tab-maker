import streamlit as st

# Page setup
st.set_page_config(page_title="Guitar Tab Maker", layout="wide")
st.title("🎸 Guitar Tab Maker")

# Constants
strings = ["E (1st)", "B (2nd)", "G (3rd)", "D (4th)", "A (5th)", "E (6th)"]
open_string_notes = ["E4", "B3", "G3", "D3", "A2", "E2"]
semitones = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
num_frets = 22

# Helper: Get note name from open note + fret
def get_note_name(open_note: str, fret: int) -> str:
    note = open_note[:-1]
    octave = int(open_note[-1])
    semitone_index = semitones.index(note) + fret
    new_octave = octave + (semitone_index // 12)
    new_note = semitones[semitone_index % 12]
    return f"{new_note}{new_octave}"

# Initialize session state
if "tab_data" not in st.session_state:
    st.session_state.tab_data = []

if "active_edit" not in st.session_state:
    st.session_state.active_edit = None  # (row, col)

# Controls
col1, col2 = st.columns([1, 2])
with col1:
    if st.session_state.tab_data:
        if st.button("↩️ Undo Last Note"):
            st.session_state.tab_data.pop()
            st.rerun()
with col2:
    if st.button("➕ Insert Pause"):
        st.session_state.tab_data.append(["-" for _ in range(6)])
        st.rerun()

# Fretboard
st.subheader("🧱 Fretboard")

header_cols = st.columns(num_frets + 1)
header_cols[0].markdown("**String**")
for fret in range(num_frets):
    header_cols[fret + 1].markdown(f"**{fret}**")

for row_idx, string in enumerate(strings):
    cols = st.columns(num_frets + 1)
    cols[0].markdown(f"**{string}**")

    for fret in range(num_frets):
        key = f"fret-{row_idx}-{fret}"
        note_name = get_note_name(open_string_notes[row_idx], fret)
        # for now, this works to make the shorter length button names a closer length to the longer ones,
        # (the ones with '#'s). this is a temporary fix and needs a cleaner, more permanent solution.
        if len(note_name) == 2:
            note_name = "\u00A0" + note_name + "\u00A0"  # Unicode non-breaking space

        if cols[fret + 1].button(note_name, key=key):
            if st.session_state.active_edit:
                r, c = st.session_state.active_edit
                st.session_state.tab_data[c][r] = str(fret)
                st.session_state.active_edit = None
                st.rerun()
            else:
                column = ["-" for _ in range(6)]
                column[row_idx] = str(fret)
                st.session_state.tab_data.append(column)
                st.rerun()

# Editable tab grid (select cell to edit)
# st.subheader("🖊️ Editable Tab Grid")
#
# if st.session_state.tab_data:
#     col_labels = st.columns(len(st.session_state.tab_data) + 1)
#     col_labels[0].markdown("**String**")
#     for i in range(len(st.session_state.tab_data)):
#         col_labels[i + 1].markdown(f"**{i + 1}**")
#
#     for row_idx, string in enumerate(strings):
#         row_cols = st.columns(len(st.session_state.tab_data) + 1)
#         row_cols[0].markdown(f"**{string}**")
#
#         for col_idx in range(len(st.session_state.tab_data)):
#             val = st.session_state.tab_data[col_idx][row_idx]
#             key = f"tabcell-{row_idx}-{col_idx}"
#             label = f"[{val}]" if (row_idx, col_idx) == st.session_state.active_edit else val
#
#             if row_cols[col_idx + 1].button(label, key=key):
#                 st.session_state.active_edit = (row_idx, col_idx)

# Formatted tab output
st.subheader("🎼 Tab Output")

string_label_width = 8
output_lines = []

# Detect widest cell to determine spacing
column_width = 2
if st.session_state.tab_data:
    for col in st.session_state.tab_data:
        for val in col:
            if val != "-" and len(val) > column_width:
                column_width = len(val)

column_width += 1  # padding

for row_idx, string in enumerate(strings):
    line = string.ljust(string_label_width) + "|"
    for col in st.session_state.tab_data:
        val = col[row_idx]
        val = val.center(column_width)[:column_width]
        line += val
    output_lines.append(line)

tab_output = "\n".join(output_lines)
st.markdown("```text\n" + tab_output + "\n```")
