Author: Saksh Menon

The purpose of this script is to make python more dynamic. This is majorly acheived by inspecting the stack. 
The get_dynamic_re function is responsible for parsing through the stacks in the order in which they were created.
Free variables are left unassigned to avoid overwritting desired values. Future implementations will attempt to call an UnboundLocalError when variables are called before their values are assigned.