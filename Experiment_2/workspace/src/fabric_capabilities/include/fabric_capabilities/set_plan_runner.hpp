#pragma once

#include <thread>

#include <rclcpp/rclcpp.hpp>
#include <rclcpp_action/rclcpp_action.hpp>

#include <capabilities2_runner/service_runner.hpp>
#include <fabric_msgs/srv/set_fabric_plan.hpp>

namespace capabilities2_runner
{

/**
 * @brief Executor runner class
 *
 * Class to run capabilities2 executor action based capability
 *
 */
class FabricSetPlanRunner : public ServiceRunner<fabric_msgs::srv::SetFabricPlan>
{
public:
  FabricSetPlanRunner() : ServiceRunner()
  {
  }

  /**
   * @brief Starter function for starting the action runner
   *
   * @param node shared pointer to the capabilities node. Allows to use ros node related functionalities
   * @param run_config runner configuration loaded from the yaml file
   * @param bond_id bond id for the runner instance, used for event emission and tracking
   */
  virtual void start(rclcpp::Node::SharedPtr node, const runner_opts& run_config, const std::string& bond_id) override
  {
    init_service(node, run_config, "/fabric/set_plan");

    // emit start event
    emit_started(bond_id, "", param_on_started());
  }

protected:
  /**
   * @brief Generate service request from event parameters
   *
   * This function is used to create a service request based on the parameters received from the trigger event. It
   * extracts necessary information from the parameters and populates the service request accordingly.
   * 
   * @param parameters EventParameters containing parameters from the trigger event
   * @return fabric_msgs::srv::SetFabricPlan::Request populated service request to be sent to the service server
   */
  virtual fabric_msgs::srv::SetFabricPlan::Request
  generate_request(capabilities2_events::EventParameters& parameters) override
  {
    fabric_msgs::srv::SetFabricPlan::Request request;
    request.plan = std::any_cast<std::string>(parameters.get_value("ReceivedPlan", std::string{}));

    return request;
  }
};

}  // namespace capabilities2_runner
