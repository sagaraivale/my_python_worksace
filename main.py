import re

xy=""" | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `block in create_with_logging_context'
2017-06-02 20:36:57 e55461bb [foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
 | ActiveRecord::RecordInvalid: Validation failed: Resource can't be blank
 | /opt/rh/rh-ror41/root/usr/share/gems/gems/activerecord-4.1.5/lib/active_record/validations.rb:57:in `save!'

 | /usr/share/gems/gems/passenger-4.0.18/lib/phusion_passenger/request_handler.rb:441:in `block (3 levels) in start_threads'
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `call'
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `block in create_with_logging_context'
2017-06-02 20:36:57 6257c4a6 [foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
 | ActiveRecord::RecordInvalid: Validation failed: Resource can't be blank
 | /opt/rh/rh-ror41/root/usr/share/gems/gems/activerecord-4.1.5/lib/active_record/validations.rb:57:in `save!'
 | /opt/rh/rh-ror41/root/usr/share/gems/gems/activerecord-4.1.5/lib/active_record/attribute_methods/dirty.rb:29:in `save!'

 | /usr/share/gems/gems/passenger-4.0.18/lib/phusion_passenger/request_handler/thread_handler.rb:108:in `main_loop'
 | /usr/share/gems/gems/passenger-4.0.18/lib/phusion_passenger/request_handler.rb:441:in `block (3 levels) in start_threads'
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `call'
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `block in create_with_logging_context'
2017-06-02 20:37:08 255ebd17 [foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
 | ActiveRecord::RecordInvalid: Validation failed: Resource can't be blank

 | /usr/share/gems/gems/passenger-4.0.18/lib/phusion_passenger/request_handler/thread_handler.rb:140:in `accept_and_process_next_request'
 | /usr/share/gems/gems/passenger-4.0.18/lib/phusion_passenger/request_handler/thread_handler.rb:108:in `main_loop'
 | /usr/share/gems/gems/passenger-4.0.18/lib/phusion_passenger/request_handler.rb:441:in `block (3 levels) in start_threads'
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `call'
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `block in create_with_logging_context'
2017-06-02 20:37:09 c84f0361 [foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
 | /opt/theforeman/tfm/root/usr/share/gems/gems/logging-1.8.2/lib/logging/diagnostic_context.rb:323:in `block in create_with_logging_context'
2017-06-02 20:40:56  [foreman-tasks/action] [E] ERF22-6719 [ForemanTasks::Task::TaskCancelledException]: Cancel enforced: the task might be still running on the Capsule (ForemanTasks::Task::TaskCancelledException)
 |
2017-06-02 20:40:56  [foreman-tasks/action] [E] ERF22-6719 [ForemanTasks::Task::TaskCancelledException]: Cancel enforced: the task might be still running on the Capsule (ForemanTasks::Task::TaskCancelledException)
 |
2017-06-02 20:40:56  [foreman-tasks/action] [E] ERF22-6719 [ForemanTasks::Task::TaskCancelledException]: Cancel enforced: the task might be still running on the Capsule (ForemanTasks::Task::TaskCancelledException)
 |
2017-06-02 20:43:31  [foreman-tasks/dynflow] [I] start terminating clock...
2017-06-02 20:46:22  [foreman-tasks/action] [E] Script execution failed
2017-06-02 20:46:22  [foreman-tasks/action] [E] Script execution failed
2017-06-02 20:46:22  [foreman-tasks/action] [E] Script execution failed
2017-06-02 20:46:22  [foreman-tasks/action] [E] Script execution failed
2017-06-02 20:46:50 c6f25aa9 [app] [F]
"""

found = re.findall(r'\[\w+.-\w+./.+',xy)
###########  command line op  ##############
"""
[foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
[foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
[foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
[foreman-tasks/dynflow] [W] Error on on_execution_plan_save event
[foreman-tasks/action] [E] ERF22-6719 [ForemanTasks::Task::TaskCancelledException]: Cancel enforced: the task might be still running on the Capsule (ForemanTasks::Task::TaskCancelledException)
[foreman-tasks/action] [E] ERF22-6719 [ForemanTasks::Task::TaskCancelledException]: Cancel enforced: the task might be still running on the Capsule (ForemanTasks::Task::TaskCancelledException)
[foreman-tasks/action] [E] ERF22-6719 [ForemanTasks::Task::TaskCancelledException]: Cancel enforced: the task might be still running on the Capsule (ForemanTasks::Task::TaskCancelledException)
[foreman-tasks/dynflow] [I] start terminating clock...
[foreman-tasks/action] [E] Script execution failed
[foreman-tasks/action] [E] Script execution failed
[foreman-tasks/action] [E] Script execution failed
[foreman-tasks/action] [E] Script execution failed

"""
#found = re.findall(r'([\w\[\-\/\]]+)\s+\[[E]\]\s+([\w\s]+)',xy)
for bae in found:
    print bae
