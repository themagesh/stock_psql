# from celery import shared_task
# from .management.commands.update_stock_prices import Command

# @shared_task
# def update_stock_prices_task():
#     command = Command()
#     command.handle()

from celery import shared_task

@shared_task
def test_task():
    return 'Task executed successfully!'