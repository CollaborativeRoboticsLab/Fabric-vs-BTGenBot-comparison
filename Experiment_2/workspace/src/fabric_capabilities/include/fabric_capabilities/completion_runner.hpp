#pragma once
#include <string>
#include <pluginlib/class_list_macros.hpp>
#include <capabilities2_runner/service_runner.hpp>
#include <fabric_msgs/srv/complete_fabric.hpp>

namespace capabilities2_runner
{
/**
 * @brief completion runner
 *
 * This class is a wrapper around the capabilities2 service runner and is used to
 * call on the /fabric/set_completion service, providing it as a
 * capability that notifys the completion of the fabric
 */
class FabricCompletionRunner : public ServiceRunner<fabric_msgs::srv::CompleteFabric>
{
public:
  FabricCompletionRunner() : ServiceRunner()
  {
  }

  /**
   * @brief Starter function for starting the service runner
   *
   * @param node shared pointer to the capabilities node. Allows to use ros node related functionalities
   * @param run_config runner configuration loaded from the yaml file
   */
  virtual void start(rclcpp::Node::SharedPtr node, const runner_opts& run_config, const std::string& bond_id) override
  {
    init_service(node, run_config, "/fabric/set_completion");

    // emit start event
    emit_started(bond_id, "", param_on_started());
  }

protected:
  /**
   * @brief generate a service request from the event parameters provided in the trigger function
   * 
   * @param parameters EventParameters containing parameters for the trigger event
   * @return CompleteFabric::Request the service request to be sent to the service server
   */
  virtual typename fabric_msgs::srv::CompleteFabric::Request
  generate_request(capabilities2_events::EventParameters& parameters) override
  {
    fabric_msgs::srv::CompleteFabric::Request request;
    request.plan_id = std::any_cast<std::string>(parameters.get_value("plan_id", std::string{}));
    return request;
  }
};

}  // namespace capabilities2_runner
