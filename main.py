RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'

SEP_COUNT = 3

print(f"""{RED}                     {END}
{RED}         {WHITE}   {RED}         {END}
{RED}      {WHITE}         {RED}      {END}
{RED}         {WHITE}   {RED}         {END}
{RED}                     {END}""")

for _ in range(SEP_COUNT):
    print()

COUNT = 6
print(f"   {WHITE}         {END}   " * COUNT)
print(f" {WHITE}   {END}       {WHITE}   {END} " * COUNT)
print(f"{WHITE}  {END}           {WHITE}  {END}" * COUNT)
print(f"{WHITE} {END}             {WHITE} {END}" * COUNT)
print(f"{WHITE}  {END}           {WHITE}  {END}" * COUNT)
print(f" {WHITE}   {END}       {WHITE}   {END} " * COUNT)
print(f"   {WHITE}         {END}   " * COUNT)
