from behave import *
from coffee_machine import Coffee_Machine

# GIVEN
@given('the machine has no water')
def step_impl(context):
	context.coffee_machine = Coffee_Machine(power_on=False)
	context.coffee_machine.has_water = False

  
@given('the machine has water')
def step_impl(context):
	context.coffee_machine = Coffee_Machine(power_on=False)
	context.coffee_machine.has_water = True

# WHEN  
@when('I switch it on')
def step_impl(context):
	context.coffee_machine.power_on = True

  
@when('I add water')
def step_impl(context):
	context.coffee_machine.add_water()

# THEN
@then('the machine should have water')
def step_impl(context):
	assert context.coffee_machine.has_water is True

  
@then('the menu should be inaccessible')
def step_impl(context):
	accessible = context.coffee_machine.show_menu()
	assert accessible is False

  
@then('a warning should be displayed')
def step_impl(context):
	displayed = context.coffee_machine.show_warning()
	assert displayed is True

  
@then('the menu should be accessible')
def step_impl(context):
	accessible = context.coffee_machine.show_menu()
	assert accessible is True
