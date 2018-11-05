/**
 * Created by 张苗 on 2018/9/7 15:07
 * Develop by 张苗 on 2018/9/7 15:07
 */
import React from 'react';
import { Table } from 'antd';
// import PropTypes from 'prop-types';
const { Column } = Table;
class CourseSchedule extends React.Component {
  renderSchedule = data => (
    <Table dataSource={data} pagination={false}>
      <Column dataIndex="lesson" key="one" />
      <Column title="周一" dataIndex="monday" key="monday" />
      <Column title="周二" dataIndex="tuesday" key="tuesday" />
      <Column title="周三" dataIndex="wednesday" key="wednesday" />
      <Column title="周四" dataIndex="thursday" key="thursday" />
      <Column title="周五" dataIndex="friday" key="friday" />
    </Table>
  );

  render() {
    const data = [
      {
        key: '1',
        lesson: '1',
        monday: '第一节课',
        tuesday: 'hah',
      }, {
        key: '2',
        lesson: '2',
        monday: 'mei',
      }, {
        key: '3',
        lesson: '3',
        friday: 'ene',
      }, {
        key: '4',
        lesson: '4',
      }, {
        key: '5',
        lesson: '5',
        thursday: 'aQQQ',
      }, {
        key: '6',
        lesson: '6',
      }, {
        key: '7',
        lesson: '7',
      },
    ];
    return (
      <div>
        {this.renderSchedule(data)}
      </div>
    );
  }
}
CourseSchedule.propTypes = {

};
export default CourseSchedule;
