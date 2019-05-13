// Code generated by protoc-gen-validate
// source: envoy/service/load_stats/v2/lrs.proto
// DO NOT EDIT!!!

package v2

import (
	"bytes"
	"errors"
	"fmt"
	"net"
	"net/mail"
	"net/url"
	"regexp"
	"strings"
	"time"
	"unicode/utf8"

	"github.com/gogo/protobuf/types"
)

// ensure the imports are used
var (
	_ = bytes.MinRead
	_ = errors.New("")
	_ = fmt.Print
	_ = utf8.UTFMax
	_ = (*regexp.Regexp)(nil)
	_ = (*strings.Reader)(nil)
	_ = net.IPv4len
	_ = time.Duration(0)
	_ = (*url.URL)(nil)
	_ = (*mail.Address)(nil)
	_ = types.DynamicAny{}
)

// Validate checks the field values on LoadStatsRequest with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *LoadStatsRequest) Validate() error {
	if m == nil {
		return nil
	}

	if v, ok := interface{}(m.GetNode()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return LoadStatsRequestValidationError{
				Field:  "Node",
				Reason: "embedded message failed validation",
				Cause:  err,
			}
		}
	}

	for idx, item := range m.GetClusterStats() {
		_, _ = idx, item

		if v, ok := interface{}(item).(interface{ Validate() error }); ok {
			if err := v.Validate(); err != nil {
				return LoadStatsRequestValidationError{
					Field:  fmt.Sprintf("ClusterStats[%v]", idx),
					Reason: "embedded message failed validation",
					Cause:  err,
				}
			}
		}

	}

	return nil
}

// LoadStatsRequestValidationError is the validation error returned by
// LoadStatsRequest.Validate if the designated constraints aren't met.
type LoadStatsRequestValidationError struct {
	Field  string
	Reason string
	Cause  error
	Key    bool
}

// Error satisfies the builtin error interface
func (e LoadStatsRequestValidationError) Error() string {
	cause := ""
	if e.Cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.Cause)
	}

	key := ""
	if e.Key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sLoadStatsRequest.%s: %s%s",
		key,
		e.Field,
		e.Reason,
		cause)
}

var _ error = LoadStatsRequestValidationError{}

// Validate checks the field values on LoadStatsResponse with the rules defined
// in the proto definition for this message. If any rules are violated, an
// error is returned.
func (m *LoadStatsResponse) Validate() error {
	if m == nil {
		return nil
	}

	if len(m.GetClusters()) < 1 {
		return LoadStatsResponseValidationError{
			Field:  "Clusters",
			Reason: "value must contain at least 1 item(s)",
		}
	}

	if v, ok := interface{}(m.GetLoadReportingInterval()).(interface{ Validate() error }); ok {
		if err := v.Validate(); err != nil {
			return LoadStatsResponseValidationError{
				Field:  "LoadReportingInterval",
				Reason: "embedded message failed validation",
				Cause:  err,
			}
		}
	}

	return nil
}

// LoadStatsResponseValidationError is the validation error returned by
// LoadStatsResponse.Validate if the designated constraints aren't met.
type LoadStatsResponseValidationError struct {
	Field  string
	Reason string
	Cause  error
	Key    bool
}

// Error satisfies the builtin error interface
func (e LoadStatsResponseValidationError) Error() string {
	cause := ""
	if e.Cause != nil {
		cause = fmt.Sprintf(" | caused by: %v", e.Cause)
	}

	key := ""
	if e.Key {
		key = "key for "
	}

	return fmt.Sprintf(
		"invalid %sLoadStatsResponse.%s: %s%s",
		key,
		e.Field,
		e.Reason,
		cause)
}

var _ error = LoadStatsResponseValidationError{}
