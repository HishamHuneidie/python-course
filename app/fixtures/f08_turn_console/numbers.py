from typing import Callable, Generator


def ticket_decorator(method: Callable) -> Callable:
    def decorated_method(ticket_type: str):
        ticket_generator = method(ticket_type)

        while True:
            print('------------------')
            print('Your turn is:')
            print(next(ticket_generator))
            print('Wait for your turn')
            print('------------------')
            yield

    return decorated_method


@ticket_decorator
def generate_ticket(ticket_type: str) -> Generator[str, None, None]:
    letter = None
    if ticket_type == 'Pharmacy': letter = 'F'
    elif ticket_type == 'Cosmetics': letter = 'C'
    elif ticket_type == 'Perfumes': letter = 'P'

    num = 1
    while True:
        yield f"{letter}-{num}"
        num += 1
