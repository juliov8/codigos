import random, datetime
# import uuid


def generate_random_timestamp(start_date, end_date):
    time_between_dates = end_date - start_date
    random_number_of_days = random.randrange(time_between_dates.days)
    random_seconds = random.randint(0, 86400)  # 86400 seconds in a day
    random_timestamp = start_date + datetime.timedelta(
        days=random_number_of_days, seconds=random_seconds
    )
    return random_timestamp


FECHA_INICIO_TRANSACCION = datetime.datetime(2023, 1, 1)
FECHA_FIN_TRANSACCION = datetime.datetime(2023, 12, 31)

FECHA_INICIO_CREACION = datetime.datetime(2000, 1, 1)
FECHA_FIN_CREACION = datetime.datetime(2020, 12, 31)

CANTIDAD_DE_USUARIOS = 20
CANTIDAD_DE_TRANSACCIONES = 200
ID_USUARIOS = []

TIPO_TRANSACCION = ["DEPOSITO", "RETIRO"]
PRIMER_NOMBRE = [
    "MANUFACTURERA", "SOLDADURIA", "DISTRIBUIDORA", "CONFECCIONES",
    "TEXTILERIA", "FARMACIA", "PANADERIA", "ZAPATERIA",
    "AUTOMOTRIZ", "MINERA", "CONSTRUCTORA", "CERVECERIA",    
]
SEGUNDO_NOMBRE = [
    "JIMENEZ", "GALARZA", "GONZALES", "RODRIGUEZ",
    "PAREDES", "GARCIA", "GAMARRA", "GUTIERREZ",
    "ALVARADO", "RAMIREZ", "HERRERA", "FIGUEROA",
]
TIPO_EMPRESA = ["SAC", "SA", "SRL", "EIRL", "SAA"]
MONEDA = ["PEN", "USD"]

for e in range(CANTIDAD_DE_USUARIOS):
    # ID_USUARIOS.append(str(uuid.uuid4()))
    ID_USUARIOS.append(random.randint(10**7, 10**8-1))

# write clients
header = "id_usuario,razon_social,ruc,email_contacto,fecha_creacion\n"
with open("clientes.csv", "w", encoding="utf-8") as f:
    f.write(header)
    for e in ID_USUARIOS:
        primer_nombre = random.choice(PRIMER_NOMBRE)
        segundo_nombre = random.choice(SEGUNDO_NOMBRE)

        s = (
            f"{e},"
            + f"{primer_nombre} {segundo_nombre} {random.choice(TIPO_EMPRESA)},"
            + f"20{random.randint(10**11, 10**12-1)},"
            + f"contacto@{(primer_nombre + segundo_nombre).lower()}.com,"
            + f"{str(generate_random_timestamp(FECHA_INICIO_CREACION, FECHA_FIN_CREACION))[:10]}"
        )
        f.write(s + "\n")

# write transactions
header = "id_usuario,tipo_transaccion,moneda,cantidad,fecha_transaccion\n"
with open("transacciones.csv", "w", encoding="utf-8") as f:
    f.write(header)
    for _ in range(CANTIDAD_DE_TRANSACCIONES):
        s = (
            f"{random.choice(ID_USUARIOS)},"
            + f"{random.choice(TIPO_TRANSACCION)},"
            + f"{random.choice(MONEDA)},"
            + f"{random.randint(1000, 5000)}.{('00' + str(random.randint(0, 99)))[-2:]},"
            + f"{generate_random_timestamp(FECHA_INICIO_TRANSACCION, FECHA_FIN_TRANSACCION)}"
        )
        f.write(s + "\n")
