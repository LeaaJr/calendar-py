import calendar

def mostrar_calendario(año, mes, label):
    calendario = calendar.TextCalendar(calendar.SUNDAY)
    calendario_str = calendario.formatmonth(año, mes)
    
    label.config(text=calendario_str)