// Auto-generated. Do not edit!

// (in-package challenge.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class CustomMessage {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.number_1 = null;
      this.number_2 = null;
    }
    else {
      if (initObj.hasOwnProperty('number_1')) {
        this.number_1 = initObj.number_1
      }
      else {
        this.number_1 = 0;
      }
      if (initObj.hasOwnProperty('number_2')) {
        this.number_2 = initObj.number_2
      }
      else {
        this.number_2 = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type CustomMessage
    // Serialize message field [number_1]
    bufferOffset = _serializer.uint32(obj.number_1, buffer, bufferOffset);
    // Serialize message field [number_2]
    bufferOffset = _serializer.uint32(obj.number_2, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type CustomMessage
    let len;
    let data = new CustomMessage(null);
    // Deserialize message field [number_1]
    data.number_1 = _deserializer.uint32(buffer, bufferOffset);
    // Deserialize message field [number_2]
    data.number_2 = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'challenge/CustomMessage';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a943712877e7ef9d7005faad2d1b0651';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint32 number_1
    uint32 number_2
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new CustomMessage(null);
    if (msg.number_1 !== undefined) {
      resolved.number_1 = msg.number_1;
    }
    else {
      resolved.number_1 = 0
    }

    if (msg.number_2 !== undefined) {
      resolved.number_2 = msg.number_2;
    }
    else {
      resolved.number_2 = 0
    }

    return resolved;
    }
};

module.exports = CustomMessage;
